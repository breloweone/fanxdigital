# FANX – Digital Service Economy Simulator
*Power to the Time, Value to the People.*

Bu depo; FANX kapalı devre dijital hizmet ekonomisinin **çalışan bir simülasyonunu** içerir.

Amaçlar:
- Yatırımcıya ekonomik ölçeklenme mantığını göstermek,
- Regülatöre “yatırım ürünü değil, hizmet ekonomisi” olduğunu ispatlamak,
- Topluluğa “emeğin nasıl değere dönüştüğünü” şeffaf göstermek,
- Teknik ekibe formülleri / parametreleri tek yerde vermek.

---

## 🔁 Temel Döngü
`User Activity → XP → Credit → Burn/Buyback → Supply↓ → Value↑ → NEV↑ → Reward → Motivation↑`

Daha matematiksel ifade ile:

1. Kullanıcı platformda içerik üretir, izler, paylaşır, mesajlaşır → **XP** kazanır.
2. XP, DAO'nun tanımladığı katsayıyla **Credit**’e (FANX Credit) dönüşür.
3. Her işlemde mikro-yakım (**burn**) + gerektiğinde **buyback** çalışır → arz azalır.
4. Arz azalırken ekosistem geliri NEV büyür → birim Credit değeri (**Value**) artma eğilimine girer.
5. Fan Pool (≈%40) NEV’den hizmet karşılığı ödül dağıtır → bu ödül **temettü değildir**; TBK m.393'e göre ifa edilmiş dijital hizmet bedelidir.
6. Cashout, pasif gelir değil; “hizmet bedeli iadesi”dir.

---

## 🧠 Hukuki Çerçeve (Özet)
- **TBK m.393-394**: XP → Credit → Cashout = ifa edilen hizmetin bedeli.
  Bu pasif yatırım getirisi değildir.
- **FSEK**: Creator mali hak sahibi olarak kalır; Fan sadece “non-exclusive kullanım lisansı” alır.
- **MiCA / VARA / SPK**: FANX Credit dışarı transfer edilemez, alınıp satılamaz, spekülatif menkul kıymet değildir.
  “Kapalı devre dijital hizmet kredisi” olarak çalışır.
- **MASAK / FATF**: Cashout’ta KYC zorunlu, limitli, kayıt altındadır. Kara para altyapısı değildir.

Bu paket, SPK ve MASAK'a “Biz Ponzi, bahis, temettü sunmuyoruz.” cevabını;
yatırımcıya da “Bu sistem gerçek ekonomik aktiviteyle çalışıyor.” cevabını
tek ekranda verebilmeniz içindir.

---

## 📂 Klasör Yapısı

```text
FANX-DigitalServiceEconomy/
├─ README.md                   → Proje özeti, ekonomi döngüsü
├─ LICENSE.txt                 → MIT lisansı
├─ SECURITY_REGULATORY.md      → Hukuki/regülasyon güvenlik notları
├─ data/
│   └─ default_parameters.json → Varsayılan katsayılar, limitler
├─ core/
│   ├─ economics.py            → XP, Credit, Burn, NEV hesap motoru
│   ├─ stress_test.py          → Hızlı büyüme / durgunluk / kötüye kullanım senaryoları
│   └─ legal.py                → Hukuki sınıflandırma yardımcıları
├─ app/
│   ├─ config.py               → Sabitler, havuz yüzdeleri
│   └─ utils.py                → Ortak yardımcı fonksiyonlar
├─ pages/
│   ├─ 1_Fan_User_Dashboard.py         → Kullanıcı (Fan) XP / Credit / Cashout görünümü
│   ├─ 2_Creator_Telif.py              → Creator telif / lisans / gelir
│   ├─ 3_Sponsor_Revenue.py            → Sponsor & Premium gelir akışı
│   ├─ 4_Supply_Burn_Buyback.py        → Arz, yakım, buyback, deflasyon
│   ├─ 5_NEV_Cashout.py                → NEV, Value, Reward dağıtımı, Cashout uygunluğu
│   └─ 6_Legal_View.py                 → SPK / MASAK / MiCA uyum paneli
├─ docs/
│   ├─ SECTION_01_Vizyon.md
│   ├─ SECTION_02_XP_System.md
│   ├─ SECTION_03_Gorev_XP_AI.md
│   ├─ SECTION_04_Finansal_Projeksiyon.md
│   ├─ SECTION_05_Icerik_Telif.md
│   ├─ SECTION_06_Deflasyonist_Arz.md
│   ├─ SECTION_07_DAO_Yonetimi.md
│   ├─ SECTION_08_NEV.md
│   ├─ SECTION_09_Cashout.md
│   ├─ SECTION_10_Hukuki_Uyum_Haritasi.md
│   ├─ SECTION_11_Yatirimci_Teklifi.md
│   └─ SECTION_12_Anayasa.md
└─ .streamlit/
    └─ config.toml             → Streamlit tema bilgisi (opsiyonel)
```

---

## 🚀 Lokal Çalıştırma (Streamlit)

1. Python 3.10+ kurulu olsun.
2. Sanal ortam (opsiyonel ama tavsiye):  
   `python -m venv venv && source venv/bin/activate`  (Windows: `venv\Scripts\activate`)
3. Gerekli paketleri kur:  
   `pip install streamlit`
4. Uygulamayı başlat:  
   `streamlit run pages/1_Fan_User_Dashboard.py`

Streamlit otomatik olarak diğer sayfaları (`pages/2_...`, `pages/3_...` vb.) yan menüde gösterir.

---

## ☂ Regülasyon Güvencesi

Bu proje yatırım tavsiyesi değildir. Buradaki sayısal sonuçlar,
FANX modelinin teorik/teknik davranışını göstermek içindir.
Hiçbir çıktı; “kâr garantisi”, “pasif getiri”, “temettü dağıtımı”, “yatırım fırsatı” ifadesi olarak
yorumlanamaz. Cashout, TBK m.393 uyarınca ifa edilmiş dijital hizmet bedelidir;
şans, bahis, yatırım veya menkul kıymet geliri değildir.

Son güncelleme: 2025-11-01
