# Regülasyon, Güvenlik ve Hukuki Çerçeve

Bu dosya, FANX simülasyonunun hukuki sınıflandırmasını ve regülasyonla uyumunu tek yerde tutar.
Bu metin pitch deck, regülatör toplantısı ve yatırımcı görüşmelerinde doğrudan referans olarak kullanılabilir.

## 1. Temel Hukuki Pozisyon
FANX bir "dijital hizmet ekonomisi"dir.
- Kullanıcı para koyup pasif getiri bekleyen bir "yatırımcı" değildir.
- Kullanıcı, platformda dijital hizmet ifa eder (içerik üretimi, paylaşım, izleme, etkileşim, moderasyon katkısı).
  Bu ifanın karşılığı olarak XP kazanır.
- XP, sistemin belirlediği katsayıya göre Credit'e dönüşür.
- Credit talep halinde cashout edilebilir; bu işlem, Türk Borçlar Kanunu (TBK) m.393 kapsamında
  "ifa edilen hizmetin bedelinin ödenmesi"dir.

Bu nedenle:
- Bu yapı **temettü değildir** (şirket kârı dağıtımı yoktur).
- **faiz değildir** (sermayenin zaman karşılığı getirisi yoktur).
- **bahis/kumar değildir** (şansa dayalı kazanç yoktur).
- **yatırım sözleşmesi değildir** (pasif getiri vaadi yoktur).

## 2. SPK Açısından
- SPKn. m.3 uyarınca "yatırım sözleşmesi", sermaye koyup pasif gelir beklentisiyle hak kazanılan menfaatlerdir.
- FANX'te gelir, pasif değil aktiftir: Kullanıcı üretir, görev yapar, katkı sağlar.
- Dolayısıyla FANX Credit, menkul kıymet değildir.

## 3. MASAK / FATF Açısından
- Cashout öncesi KYC zorunludur.
- Cashout limitlidir (günlük / haftalık / aylık).
- Transfer yalnızca kullanıcıya kayıtlı tekil IBAN/ödeme kanalına yapılır.
- Peer-to-peer serbest transfer yoktur.
- Bu yapı kara para aklamayı zorlaştırır, MASAK uyumunu güçlendirir.

FATF VASP kriterleri bakımından:
- FANX Credit dışarı transferable değildir.
- Bu nedenle "Virtual Asset Service Provider" statüsü doğmaz.

## 4. MiCA / AB Açısından
- MiCA, transfer edilebilen, dolaşabilen kripto varlıkları düzenler.
- FANX Credit kapalı devredir ve dış borsada alınıp satılamaz.
- Bu yüzden MiCA lisansı gerekmez.

## 5. Telif / FSEK Açısından
- Creator, eserin mali hak sahibidir.
- Fan bir "non-exclusive kullanım lisansı" alır (FSEK m.52).
- Platform yalnızca aracı hizmet sağlayıcıdır (FSEK m.77/A).
- Bu yapı telif zincirini hukuki olarak savunulabilir kılar.

## 6. Neden Ponzi Değil?
- Ponzi şeması yeni para girmesine bağımlıdır.
- FANX döngüsü ise içsel etkileşime bağımlıdır:
  Kullanıcı üretir → satış olur → yakım olur → arz düşer → değer artar → motivasyon oluşur.
- Yani değer dışarıdan gelen yatırımdan değil, içeride üretilen faaliyetten doğar.

## 7. DAO ve Şeffaflık
DAO aşağıdakileri belirler ve halka açık ilan eder:
- Yakım oranları (αₜ)
- Buyback oranı (ρₜ)
- R_conv (XP → Credit dönüşüm katsayısı)
- Havuz yüzdeleri (Fan / Creator / DAO / Platform)

Bunlar tek kişinin keyfi kararı değildir ve değiştirildiğinde delil niteliğinde kayıt altına alınır.

## 8. Uyarı (Slide Altı Zorunlu Metin)
"Bu doküman, FANX Ekonomisi'nin kapalı devre dijital hizmet modelinin teknik simülasyonunu göstermek amacıyla hazırlanmıştır.
Buradaki hiçbir değer, sabit getiri taahhüdü, yatırım tavsiyesi, menkul kıymet arzı veya pasif gelir vaadi değildir.
Kullanıcıların elde ettiği kazançlar, TBK m.393 kapsamında ifa edilmiş dijital hizmet bedelidir."
