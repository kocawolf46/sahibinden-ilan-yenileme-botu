sahibinden ilan araba motor parça yenileme botu
Python kurulum ve bot çalıştırma için lazım olan her şey:

1. Python'u kurduysan önce bunu yap:

Cmd'yi aç (Win+R -> cmd) ve sırayla:

Code
python --version
Python 3.13.x yazması lazım.

2. Gerekli kütüphaneleri kur (tek satır):

Code
python -m pip install --upgrade pip
python -m pip install selenium webdriver-manager python-dotenv
3. Botu çalıştır:

Bot dosyan C:\sahibinden-bot içindeyse:

Code
cd C:\sahibinden-bot
python motor_parca_bot.py
requirements.txt ile kurmak istersen:

requirements.txt diye dosya oluştur, içine bunu yapıştır:

Code
selenium
webdriver-manager
python-dotenv
Sonra:

Code
python -m pip install -r requirements.txt
Senin son dosyan zaten hazır, ekstra bir şey kurmana gerek yok. O 2 kütüphane (selenium + webdriver-manager) yetiyor.

