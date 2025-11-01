import streamlit as st
from core.legal import legal_flags

st.set_page_config(page_title="FANX • Legal View", page_icon="⚖️")

st.title("⚖️ Hukuki / Regülasyon Görünümü")
st.caption("Bu ekran SPK, MASAK, MiCA, FSEK ve TBK açısından projenin statüsünü özetler.")

st.header("Parametreler")
col1, col2, col3 = st.columns(3)
with col1:
    transferable = st.checkbox("Credit transfer edilebilir mi?", value=False)
    cashout_contrib = st.checkbox("Cashout emeğe bağlı mı?", value=True)
with col2:
    kyc_enabled = st.checkbox("KYC aktif mi?", value=True)
    cashout_limits = st.checkbox("Cashout limitleri var mı?", value=True)
with col3:
    creator_rights = st.checkbox("Creator mali hak sahibi mi?", value=True)
    fan_license_only = st.checkbox("Fan sadece lisans mı alıyor?", value=True)

flags = legal_flags(
    transferable=transferable,
    kyc_enabled=kyc_enabled,
    cashout_limits_active=cashout_limits,
    cashout_requires_contribution=cashout_contrib,
    creator_keeps_rights=creator_rights,
    fan_gets_license_only=fan_license_only,
)

st.subheader("Sonuç Etiketleri")
st.json(flags)

st.divider()
st.header("Regülasyon Mesajı")
st.markdown("""
- FANX bir yatırım ürünü değildir; pasif getiri vaadi yoktur.
- SPK kapsamındaki menkul kıymetler gibi serbest dolaşıma çıkan, transfer edilebilir bir token sunulmaz.
- MiCA/VARA kapsamındaki borsa tipi token modeli yoktur.
- MASAK açısından KYC + limitli cashout mekanizması mevcuttur.
- Creator, FSEK'e göre mali hak sahibidir; Fan yalnızca kullanım lisansı alır.
- TBK m.393'e göre cashout = ifa edilmiş dijital hizmetin bedelidir, faiz/temettü değildir.
""")
