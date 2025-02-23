from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()

def sayfaGetir(url,word,baslik2):
    driver.get(url)
    link = driver.current_url
    baslik = driver.title #şuanki başlığı getirir.    
    print("baslik:"+ baslik)
    if word in link:
        print("Doğru "+ baslik2 + " Sayfasındayız:"+link)

sayfaGetir("http://apple.com","apple.com","Apple")
link = driver.current_url #şuanki linki (url) getirir.
print("Current URL:" +link)

sayfaGetir("http://www.etsy.com","etsy.com","Etsy")
link = driver.current_url #şuanki linki (url) getirir.
print("Current URL:" +link)
#driver.maximize_window() #sayfayı büyütür.
driver.close() #şuanki pencereyi kapatır.
#driver.quit() tüm pencereleri kapatır.

# time.sleep(3)
# driver.back() #sayfaya geri döndürür.
#driver.forward() #sayfayı ilerletir.
# time.sleep(5)
# driver.close() #sayfayı sonlandırır. #driver.quit() selenium kullandığı tüm pencereleri kapatır.












