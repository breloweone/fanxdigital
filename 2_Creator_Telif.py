import streamlit as st
from app.utils import format_currency
from app.config import DEFAULT_PARAMS

st.set_page_config(page_title="FANX • Creator Telif", page_icon="🎨")

st.title("🎨 Creator Telif / Lisans Geliri Simülasyonu")
st.caption("FSEK uyumlu lisans akışı • Fan 'sahip' olmaz, 'lisanslı erişim' hakkı alır.")

st.header("1️⃣ İçerik Satışı")
sold_items = st.number_input("Satılan içerik sayısı", min_value=0, value=10)
price_per_item_credit = st.number_input("İçerik başına fiyat (₣)", min_value=0.0, value=10.0, step=1.0)

total_credit_flow = sold_items * price_per_item_credit

st.write(f"Toplam FANX Credit akışı: **{total_credit_flow:.2f} ₣**")

st.subheader("Pay Dağılımı")
creator_share_ratio = 0.90
platform_share_ratio = 0.10
burn_ratio = 0.02  # her işlemde mikro yakım

creator_credit = total_credit_flow * creator_share_ratio
platform_credit = total_credit_flow * platform_share_ratio
burned_credit = total_credit_flow * burn_ratio

st.write(f"Creator payı: **{creator_credit:.2f} ₣**")
st.write(f"Platform payı: **{platform_credit:.2f} ₣**")
st.write(f"Yakılan arz (burn): **{burned_credit:.2f} ₣**  (deflasyon)")

st.divider()
st.header("2️⃣ Telifin Hukuki Niteliği")
st.markdown("""
- FSEK m.21–25 uyarınca mali haklar **Creator**'dadır.
- FSEK m.52 uyarınca **Fan sadece basit (non-exclusive) kullanım lisansı alır.**
- Platform, FSEK m.77/A anlamında **aracı hizmet sağlayıcıdır.**
- Bu gelir kalemi yatırım getirisi değil, **eser lisans bedelidir.**
""")

st.divider()
st.header("3️⃣ Ekonomik Etki")
st.markdown("""
Her satın alma olayı:
- Creator'a doğrudan telif benzeri gelir yaratır,
- Platforma operasyon bedeli bırakır,
- Arzda kalıcı yakım tetikler → deflasyon,
- Kalan Credit'lerin birim değerini orta-uzun vadede güçlendirir.
""")
