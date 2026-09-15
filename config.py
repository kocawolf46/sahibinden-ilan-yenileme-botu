"""
config.py - Sahibinden Bot Ayarları
Zam YOK modu için
"""
# Zam oranı - 0 = zam yok, aynı fiyatla yenile
# %3 zam yapmak istersen 0.03 yap, %5 için 0.05
# Fiyat düşürmek için -0.02 gibi negatif değer
ZAM_ORANI = 0

# Sadece bu ilanları yenile, boş liste = tüm aktif yedek parça ilanları
# Örnek: ["1234567890", "1122334455"]
SADECE_BU_ILANLAR = []

# Her yenilemede açıklamaya tarih eklesin mi?
YENILEME_NOTU_EKLE = False
NOT_SABLONU = "Güncel stok - {tarih}"

# Bot ne kadar beklesin? Sahibinden hızlı işlemi sevmiyor
ISLEM_ARASI_BEKLEME_SANIYE = 15

# Log dosyası adı
LOG_FILE = "yenileme_log.txt"
