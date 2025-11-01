import streamlit as st
from app.config import DEFAULT_WEIGHTS, DEFAULT_PARAMS
from core.economics import compute_xp, apply_ai_quality, apply_caps, xp_to_credit
from core.economics import check_cashout_eligibility

st.set_page_config(page_title="FANX • Fan Dashboard", page_icon="💠")

st.title("💠 FANX Closed-Loop Economy Simulator — Fan / Kullanıcı")
st.caption("XP → Credit → Cashout • Bu kazanç temettü değildir; ifa edilmiş dijital hizmet bedelidir (TBK m.393).")

st.header("1️⃣ Aktiviteni Gir (Bugün)")
col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
with col1:
    watch_minutes = st.number_input("İzleme (dk)", min_value=0, value=20)
with col2:
    share_count = st.number_input("Paylaşım", min_value=0, value=3)
with col3:
    msg_count = st.number_input("Mesaj", min_value=0, value=10)
with col4:
    upload_count = st.number_input("Upload", min_value=0, value=1)
with col5:
    create_count = st.number_input("Yeni Eser", min_value=0, value=1)
with col6:
    event_count = st.number_input("Etkinlik Katılım", min_value=0, value=0)
with col7:
    invite_count = st.number_input("Davet", min_value=0, value=1)

st.subheader("Yapay Zekâ Kalite Katsayısı")
ai_score = st.slider("AI_score (0=spam, 1=organik kalite)", 0.0, 1.0, 0.9, 0.01)

# Hesapla XP
activities = {
    "WATCH": watch_minutes,
    "SHARE": share_count,
    "MESSAGE": msg_count,
    "UPLOAD": upload_count,
    "CREATE": create_count,
    "EVENT": event_count,
    "INVITE": invite_count,
}

xp_raw = compute_xp(activities, DEFAULT_WEIGHTS)
xp_real = apply_ai_quality(xp_raw, ai_score)
xp_capped = apply_caps(xp_real, DEFAULT_PARAMS["daily_cap"], DEFAULT_PARAMS["weekly_cap"])
credit_gain = xp_to_credit(xp_capped, DEFAULT_PARAMS["R_conv"])

st.markdown("### 2️⃣ Sonuçlar")
st.write(f"Brüt XP (kalite öncesi): **{xp_raw:.2f} XP**")
st.write(f"AI sonrası XP_real: **{xp_real:.2f} XP**")
st.write(f"XP (CAP sonrası): **{xp_capped:.2f} XP**")
st.write(f"Kazanılan Credit (₣): **{credit_gain:.2f} ₣**")

st.divider()

st.header("3️⃣ Cashout Uygunluğu")
st.caption("Cashout yatırım getirisi değildir. Bu, ifa edilmiş dijital hizmetin bedelinin ödenmesidir. (TBK m.393-394)")

request_amount = st.number_input("Bugün çekmek istediğin Credit (₣)", min_value=0.0, value=50.0, step=10.0)
ccs_score = st.slider("CCS (Katkı Skoru)", 0, 100, 85, 1)
premium_user = st.checkbox("Premium Creator mıyım?", value=False)

ok, reason = check_cashout_eligibility(
    credit_amount=credit_gain,
    ccs_score=ccs_score,
    cashout_limits=DEFAULT_PARAMS["cashout_limits"],
    period_request_amount=request_amount,
    is_premium=premium_user
)

st.write("Cashout Durumu:", "✅ Uygun" if ok else "⛔ Reddedildi")
st.write("Açıklama:", reason)

st.divider()
st.header("4️⃣ Hukuki Notlar")
st.markdown("""
- Bu ödül bir **temettü değildir**; pasif kazanç yoktur.
- Cashout bir **faiz** değildir; sermayeye zaman karşılığı ödeme yoktur.
- Bu sonuç bir **bahis kazancı** değildir; şans yoktur.
- Bu, kullanıcının **dijital emek karşılığıdır** ve Türk Borçlar Kanunu m.393'e tabidir.
""")
