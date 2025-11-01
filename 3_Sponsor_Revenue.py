import streamlit as st
from app.utils import format_currency, format_num

st.set_page_config(page_title="FANX • Sponsor / Premium", page_icon="💼")

st.title("💼 Sponsor & Premium Gelir Akışı")
st.caption("Bu panel yatırımcıya 'para nereden geliyor' sorusunu anlatır.")

st.header("1️⃣ Girdi Parametreleri")
sponsor_budget = st.number_input("Sponsor kampanya bütçesi ($)", min_value=0.0, value=50000.0, step=1000.0)
premium_users = st.number_input("Premium abone sayısı", min_value=0, value=20000, step=1000)
premium_fee = st.number_input("Aylık premium bedeli ($)", min_value=0.0, value=4.99, step=0.5)
message_microrev = st.number_input("Mesaj içi mikro ödemeler ($)", min_value=0.0, value=8000.0, step=500.0)
content_sales_rev = st.number_input("Lisanslı içerik satış geliri ($)", min_value=0.0, value=12000.0, step=500.0)

gross_revenue = (
    sponsor_budget
    + premium_users * premium_fee
    + message_microrev
    + content_sales_rev
)

st.markdown("### 2️⃣ Toplam Brüt Gelir (G_gross)")
st.write("Toplam:", format_currency(gross_revenue))

st.subheader("Havuzlara Bölünme")
fan_pool_ratio = 0.40
creator_pool_ratio = 0.30
dao_pool_ratio = 0.20
platform_pool_ratio = 0.10

fan_pool = gross_revenue * fan_pool_ratio
creator_pool = gross_revenue * creator_pool_ratio
dao_pool = gross_revenue * dao_pool_ratio
platform_pool = gross_revenue * platform_pool_ratio

st.write(f"Fan Pool (%40): {format_currency(fan_pool)}")
st.write(f"Creator Pool (%30): {format_currency(creator_pool)}")
st.write(f"DAO Pool (%20): {format_currency(dao_pool)}")
st.write(f"Platform Pool (%10): {format_currency(platform_pool)}")

st.divider()
st.header("3️⃣ Yorum")
st.markdown("""
- Sponsor bütçesi = topluluk görevlerini fonlayan dış para.
- Bu para Fan Pool'a akar ve aslında kullanıcı emeğini öder.
- DAO Pool içeri giren pay; buyback gücünü besler ve arzı geri çekmek için kullanılır.
- Platform payı = operasyon masrafını, moderasyon, KYC, yasal uyum maliyetlerini karşılar.
- Hiçbir kalemde "yatırımcıya temettü dağıtımı" yoktur.
""")
