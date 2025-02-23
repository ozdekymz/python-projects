
from selenium.webdriver.common.by import By #id import ettik. 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from sayfa.sayfadanVeriCekme import sayfadanVeriCek

service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()

#***Senaryomuz: bir kod yazıcaz vikipedia nın sayfasına gidip ordan 'haftanın seçkin maddesi' yazılarını çekip bize döndürecek.

#driver.get("https://tr.wikipedia.org/wiki/Anasayfa")
#seckin_madde_alani = driver.find_element(By.ID,"mp-tfa") 

#***selenium metin alırken tablara göre alınır.

#seckin_madde_yazisi = seckin_madde_alani.text
#print(seckin_madde_yazisi)

sayfadanVeriCek(driver,"https://tr.wikipedia.org/wiki/Anasayfa",By.ID,"mp-tfa")
driver.quit()











    
