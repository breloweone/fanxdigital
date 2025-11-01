from .economics import economic_tick

def scenario_fast_growth(params):
    # yüksek kullanıcı, yüksek sponsor, yüksek burn
    scenario = params.copy()
    scenario["gross_revenue_inputs"]["sponsor"] *= 2.5
    scenario["burn_volume_inputs"]["sponsor"] *= 2.0
    scenario["users_active"] *= 2.0
    return economic_tick(**scenario)

def scenario_flat(params):
    # durağan dönem: sponsor yok, burn düşük
    scenario = params.copy()
    scenario["gross_revenue_inputs"]["sponsor"] = 0.0
    scenario["burn_volume_inputs"]["sponsor"] *= 0.3
    return economic_tick(**scenario)

def scenario_attack(params):
    # bot saldırısı: XP çok yüksek ama AI_score düşük,
    # DAO R_conv düşürüyor
    scenario = params.copy()
    scenario["ai_score"] = 0.3
    scenario["R_conv"] = params["R_conv"] * 0.5
    return economic_tick(**scenario)
