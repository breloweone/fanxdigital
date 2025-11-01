import streamlit as st
from app.utils import format_num

st.set_page_config(page_title="FANX • Arz / Yakım", page_icon="🔥")

st.title("🔥 Arz • Yakım • Buyback (Deflasyonist Model)")
st.caption("Her işlem arzı azaltır; arz azaldıkça kıtlık artar. Bu fiyat pompalama değil, matematiksel kıtlık yönetimidir.")

st.header("1️⃣ Başlangıç Arz ve İşlem Hacmi")
supply_start = st.number_input("Mevcut Arz (Supply_t)", min_value=0.0, value=1_000_000_000.0, step=1_000_000.0)
sponsor_volume = st.number_input("Sponsor kaynaklı hacim (₣)", min_value=0.0, value=200000.0, step=10000.0)
message_volume = st.number_input("Mesaj hacmi (₣)", min_value=0.0, value=100000.0, step=5000.0)
content_volume = st.number_input("İçerik satış hacmi (₣)", min_value=0.0, value=50000.0, step=1000.0)

burn_rate_sponsor = st.slider("Yakım oranı (Sponsor etkileşimi %)", 0.0, 0.10, 0.05, 0.01)
burn_rate_message = st.slider("Yakım oranı (Mesaj %)", 0.0, 0.10, 0.01, 0.01)
burn_rate_content = st.slider("Yakım oranı (İçerik %)", 0.0, 0.10, 0.03, 0.01)

total_burn = (
    sponsor_volume * burn_rate_sponsor +
    message_volume * burn_rate_message +
    content_volume * burn_rate_content
)

st.write(f"Toplam Yakım (Burn_t): **{format_num(total_burn)} ₣**")

buyback = st.number_input("DAO Buyback (₣ geri çekilecek)", min_value=0.0, value=50000.0, step=1000.0)

new_supply = max(supply_start - total_burn - buyback, 0)

st.markdown("### 2️⃣ Yeni Arz")
st.write(f"Supply_t+1: **{format_num(new_supply)} ₣**  (daha kıt)")

st.divider()
st.header("3️⃣ Hukuki Yorum")
st.markdown("""
- Buyback burada **borsada fiyat pompalama değildir** çünkü halka açık spekülatif al-sat yoktur.
- Buyback sadece arzı dengelemek ve deflasyon hızını yönetmek için kullanılır.
- Bu yapı MiCA / VARA açısından "piyasa manipülasyonu" kategorisine girmez çünkü dış borsa yoktur.
""")
