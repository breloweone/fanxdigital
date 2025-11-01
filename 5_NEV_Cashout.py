import streamlit as st
from app.utils import format_currency, format_num
from app.config import DEFAULT_PARAMS
from core.economics import compute_nev, compute_value_per_credit, check_cashout_eligibility

st.set_page_config(page_title="FANX • NEV & Cashout", page_icon="💹")

st.title("💹 NEV • Value • Cashout Uygunluğu")
st.caption("NEV = G_gross - C_total. Cashout = hizmet bedeli iadesi, temettü değil.")

st.header("1️⃣ Gelir / Gider Girdileri")
col1, col2 = st.columns(2)
with col1:
    rev_sponsor = st.number_input("Sponsor geliri ($)", min_value=0.0, value=50000.0, step=1000.0)
    rev_content = st.number_input("İçerik satış geliri ($)", min_value=0.0, value=12000.0, step=1000.0)
    rev_premium = st.number_input("Premium abonelik ($)", min_value=0.0, value=20000.0, step=1000.0)
with col2:
    rev_message = st.number_input("Mesaj mikro ödeme ($)", min_value=0.0, value=8000.0, step=1000.0)
    rev_other = st.number_input("Diğer dijital gelirler ($)", min_value=0.0, value=5000.0, step=500.0)

G_gross = rev_sponsor + rev_content + rev_premium + rev_message + rev_other

st.write("Toplam Brüt Gelir (G_gross):", format_currency(G_gross))

col3, col4 = st.columns(2)
with col3:
    c_server = st.number_input("Server / AI maliyeti ($)", min_value=0.0, value=8000.0, step=500.0)
    c_ops = st.number_input("Operasyon / Moderasyon ($)", min_value=0.0, value=6000.0, step=500.0)
    c_cashout = st.number_input("Cashout ödemeleri ($)", min_value=0.0, value=7000.0, step=500.0)
with col4:
    c_reward = st.number_input("Reward dağıtımı ($)", min_value=0.0, value=10000.0, step=500.0)
    c_buyback = st.number_input("DAO buyback gideri ($)", min_value=0.0, value=4000.0, step=500.0)

C_total = c_server + c_ops + c_cashout + c_reward + c_buyback

st.write("Toplam Gider (C_total):", format_currency(C_total))

nev_val = compute_nev(G_gross, C_total)

st.markdown("### 2️⃣ NEV (Net Ekosistem Değeri)")
st.write("NEV:", format_currency(nev_val))

st.header("2️⃣.1 Arz Sonrası Değer")
current_supply = st.number_input("Güncel Arz (₣)", min_value=0.0, value=900_000_000.0, step=1_000_000.0)
value_per_credit = compute_value_per_credit(nev_val, current_supply)

st.write("Credit Başına Teorik Değer:", format_currency(value_per_credit))

st.caption("Formül: Valueₜ₊₁ = NEVₜ / Supplyₜ₊₁")

st.divider()
st.header("3️⃣ Ortalama Kullanıcı Ödülü (Fan Pool)")
users_active = st.number_input("Aktif kullanıcı sayısı", min_value=1, value=100000, step=1000)
fan_pool_ratio = DEFAULT_PARAMS['fan_pool_ratio']
reward_avg = (nev_val * fan_pool_ratio) / users_active
st.write("Kullanıcı Başına Teorik Pay (Reward_avg):", format_currency(reward_avg))
st.caption("Bu temettü değildir; pasif sermaye getirisi yoktur. Bu, kullanıcı katkı katsayısı (CCS) ile ağırlıklandırılan hizmet bedelidir.")

st.divider()
st.header("4️⃣ Cashout Hukuki Analiz")
credit_wallet = st.number_input("Cüzdandaki Credit (₣)", min_value=0.0, value=250.0, step=10.0)
want_cashout = st.number_input("Talep edilen Cashout (₣)", min_value=0.0, value=100.0, step=10.0)
user_ccs = st.slider("Kullanıcı CCS", 0, 100, 82, 1)
premium_flag = st.checkbox("Premium Creator", value=False)

ok, reason = check_cashout_eligibility(
    credit_amount=credit_wallet,
    ccs_score=user_ccs,
    cashout_limits=DEFAULT_PARAMS["cashout_limits"],
    period_request_amount=want_cashout,
    is_premium=premium_flag
)

st.write("Durum:", "✅ Onaylı" if ok else "⛔ Engellendi")
st.write("Gerekçe:", reason)

st.divider()
st.header("5️⃣ Regülatöre Verilecek Cümle")
st.markdown("""
Cashout; yatırım geliri, faiz, bahis kazancı veya temettü değildir.
Cashout; TBK m.393 kapsamında ifa edilmiş dijital hizmetin bedelinin ödenmesidir.
""")
