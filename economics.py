import math

# XP hesaplama
def compute_xp(activity_counts, weights):
    """
    activity_counts: dict {code: adet}
    weights: dict {code: katsayı w_j}
    XP_i = Σ (A_j × w_j)
    """
    xp_raw = 0.0
    for code, amount in activity_counts.items():
        w = weights.get(code, 0.0)
        xp_raw += amount * w
    return xp_raw

def apply_ai_quality(xp_raw, ai_score):
    """XP_real = XP_i × AI_score.
    ai_score 0.0 - 1.0 arası kalite katsayısı.
    """
    return xp_raw * ai_score

def apply_caps(xp_real, daily_cap, weekly_cap):
    """XP günlük/haftalık üst sınır mantığı.
    Burada basitçe günlük kapa takıyoruz çünkü sim tek periyotluk."""
    return min(xp_real, daily_cap)

def xp_to_credit(xp_real_capped, R_conv):
    """Credit = XP_real_capped × R_conv"""
    return xp_real_capped * R_conv

# CCS / Reputation tabanlı katkı gücü
def compute_ccs_score(active, quality, network, alpha=1.0, beta=1.0, gamma=1.0):
    """CCS_i = (Aktiflik×α)+(Kalite×β)+(AğEtkisi×γ)"""
    return active * alpha + quality * beta + network * gamma

# Reward dağıtımı
def compute_reward_for_user(fan_pool_value, ccs_user, ccs_all_sum):
    if ccs_all_sum <= 0:
        return 0.0
    return fan_pool_value * (ccs_user / ccs_all_sum)

# Havuz dağılımı (Fan / Creator / DAO / Platform)
def split_pools(nev_value, ratios):
    return {
        "fan_pool": nev_value * ratios["fan"],
        "creator_pool": nev_value * ratios["creator"],
        "dao_pool": nev_value * ratios["dao"],
        "platform_pool": nev_value * ratios["platform"]
    }

# Yakım & Buyback
def calc_burn(volume_by_type, burn_rates):
    """Toplam yakım = Σ(volume_type * burn_rate[type])"""
    total_burn = 0.0
    for t, vol in volume_by_type.items():
        rate = burn_rates.get(t, 0.0)
        total_burn += vol * rate
    return total_burn

def new_supply(supply_t, burn_amount, buyback_amount):
    return max(supply_t - burn_amount - buyback_amount, 0)

# NEV ve Value
def compute_nev(gross_revenue, costs_total):
    return gross_revenue - costs_total

def compute_value_per_credit(nev_value, supply_after):
    if supply_after <= 0:
        return 0.0
    return nev_value / supply_after

# Cashout eligibility
def check_cashout_eligibility(credit_amount, ccs_score, cashout_limits, period_request_amount, is_premium=False):
    """
    period_request_amount: kullanıcının bu dönem çekmek istediği Credit
    cashout_limits: {daily, weekly, monthly, premium_monthly, requires_ccs}
    """
    # yeterli CCS?
    if ccs_score < cashout_limits["requires_ccs"]:
        return False, "CCS düşük / spam şüphesi"

    # limitler
    max_allowed = cashout_limits["monthly"]
    if is_premium:
        max_allowed = cashout_limits["premium_monthly"]

    if period_request_amount > max_allowed:
        return False, "Limit aşıldı"

    if period_request_amount > credit_amount:
        return False, "Yetersiz Credit"

    return True, "Cashout onaylı (TBK m.393 hizmet bedeli iadesi)"

# High-level economic tick
def economic_tick(
    activity_counts,
    weights,
    ai_score,
    daily_cap,
    weekly_cap,
    R_conv,
    ccs_user,
    ccs_all_sum,
    gross_revenue_inputs,
    costs_inputs,
    burn_volume_inputs,
    burn_rates,
    supply_before,
    buyback_amount,
    ratios,
    users_active,
):
    """
    Tam döngü:
    - XP
    - Credit
    - Burn / Buyback / Supply
    - NEV
    - Value
    - Reward Avg
    """

    xp_raw = compute_xp(activity_counts, weights)
    xp_real = apply_ai_quality(xp_raw, ai_score)
    xp_capped = apply_caps(xp_real, daily_cap, weekly_cap)
    credit_gained = xp_to_credit(xp_capped, R_conv)

    # geliri topla
    gross_revenue = sum(gross_revenue_inputs.values())

    # maliyetleri topla
    costs_total = sum(costs_inputs.values())

    # NEV
    nev_val = compute_nev(gross_revenue, costs_total)

    # Havuz böl
    pools = split_pools(nev_val, ratios)

    # Yakım
    burn_amount = calc_burn(burn_volume_inputs, burn_rates)

    # Yeni arz
    supply_after = new_supply(supply_before, burn_amount, buyback_amount)

    # Credit değeri
    value_per_credit = compute_value_per_credit(nev_val, supply_after)

    # Ortalama kullanıcı ödülü (theoretical)
    reward_avg = 0.0
    if users_active > 0:
        reward_avg = (nev_val * ratios["fan"]) / users_active

    # Bireysel reward tahmini (CCS bazlı pay)
    reward_user = compute_reward_for_user(
        pools["fan_pool"],
        ccs_user,
        ccs_all_sum if ccs_all_sum > 0 else ccs_user
    )

    return {
        "xp_raw": xp_raw,
        "xp_real": xp_real,
        "xp_capped": xp_capped,
        "credit_gained": credit_gained,

        "gross_revenue": gross_revenue,
        "costs_total": costs_total,
        "nev": nev_val,

        "burn_amount": burn_amount,
        "supply_after": supply_after,
        "value_per_credit": value_per_credit,

        "pools": pools,
        "reward_avg": reward_avg,
        "reward_user": reward_user,
    }
