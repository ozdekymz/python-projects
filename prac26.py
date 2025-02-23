#TARAYICI AYARLARI
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.chrome.options import Options

service = Service("./chromedriver")

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-automation"]) #otomasyonu aktive eder.
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-infobars") #"chrome is automated software" üstteki yazıyı kaldırır.
options.add_argument("--allow-running-insecure-content") #sayfa güvenli olmasa da çalıştırmaya devame eder.
options.add_argument("--disable-notifications") #konum bilmek istiyor js alertleri kapatır.
options.add_argument("--disable-save-password") #password kaydetmeyi engeller.
options.add_argument("--disable-extensions") #eklentilerin hepsini kapat.
options.add_argument("download.default_directory=C:/kullanicilar/ali/test") #tarayıcıyla bişey indirdiğimizde biz indirilenler klasörünün yolunu otomatik belirleriz.
options.add_argument("--window-size=768,1024") #i-ad mini ebatlarında açması için ayarladık.
options.add_argument("--disable-popup-blocking") #pop upları bizim için kapatır.

#options.add_argument() Chrome a bir takım argumanlar ve değerler gireceğiz.

driver = webdriver.Chrome(service=service,options = options) #default ayarlar yerine benim belirlediğim ayarları uygula ve bana ver diyoruz.
#driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.ucuzabilet.com")
time.sleep(2)
driver.quit()