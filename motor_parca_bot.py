import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

ILANLAR = [
    "ilan no ları yaz",
   
]

def get_driver():
    opts = Options()
    opts.add_argument("--start-maximized")
    opts.add_argument("--disable-blink-features=AutomationControlled")
    opts.add_experimental_option("excludeSwitches", ["enable-automation"])
    opts.add_experimental_option('useAutomationExtension', False)
    service = ChromeService(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=opts)

def yenile():
    driver = get_driver()
    try:
        driver.get("https://www.sahibinden.com/giris")
        print("\n" + "="*60)
        print(f"{len(ILANLAR)} ADET ILAN YENILENECEK (ZAM YOK)")
        print("1. Acilan tarayicidan SAHIBINDEN'E GIRIS YAP")
        print("2. Giris yaptiktan sonra buraya gel ENTER'A BAS")
        print("="*60 + "\n")
        input("Giris yaptin mi? Enter -> ")

        for ilan_id in ILANLAR:
            print(f"\n-> {ilan_id} yenileniyor...")
            driver.get(f"https://www.sahibinden.com/ilan-duzenle/{ilan_id}")
            time.sleep(6)
            try:
                btn = None
                for sel in ["#saveAdButton", "button[type='submit']", "button.large"]:
                    try:
                        btn = driver.find_element(By.CSS_SELECTOR, sel)
                        if btn.is_displayed():
                            break
                    except:
                        continue
                
                if not btn:
                    print(f"  Kaydet butonu yok {ilan_id}, atlaniyor")
                    continue

                driver.execute_script("arguments[0].scrollIntoView({block:'center'});", btn)
                time.sleep(1.5)
                driver.execute_script("arguments[0].click();", btn)
                
                print(f"  ✓ {ilan_id} YENILENDI")
                time.sleep(18)

            except Exception as e:
                print(f"  ✗ {ilan_id} HATA: {e}")
                time.sleep(5)
                continue

        print("\n--- BITTI, HEPSI YENILENDI ---")
        input("Kapatmak icin Enter...")

    finally:
        driver.quit()

if __name__ == "__main__":
    yenile()
