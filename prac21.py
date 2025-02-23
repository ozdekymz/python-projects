#IFRAME İLE SAYFA İÇİNDE SAYFA: IFRAME BİR HTML SAYFASI İÇİNDE BAŞKA BİR HTML SAYFASI OLMASINA DENİR.
#Iframe tagı ise bu html sayfasını içine girerken kullandığımız tagdır.
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("./chromedriver")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://tomspizzeria.b4a.app//iframe-demo.html")
driver.switch_to.frame("email") #iframe e geçiş yaptırıyoruz. 1) iframe_id 2) iframe name 3) index (0 dan başlıyor.) 
driver.find_element(By.ID,"email").send_keys("ozde")
time.sleep(2)
#Tekrar driver nesnesini iframe den çıkarmamız gerekir.



driver.switch_to.default_content()
driver.find_element(By.ID,"isim").send_keys("ozdecikcik")
time.sleep(2)

#Burda iki seçenek var parent _frame ve default_content adında.
#Default Content: En ana sayfaya yani sayfanın aslına dönecektir.
#Parent Frame: Bir üstteki frame e geçiş sağlar.


iframeler = driver.find_elements(By.TAG_NAME,"iframe")
iframeSayisi = len(iframeler)
print(iframeSayisi)

driver.quit()