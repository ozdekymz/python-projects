#FARE HAREKETİ -- MOVE TO ELEMENT: Fareyi kullanıcı üstüne getirdiğinde görülür. (ActionChains Sınıfı Kullanarak)
import time
from baslangic import baslat
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

service = Service("./chromedriver")
driver = webdriver.Chrome(service=service)

baslat("https://the-internet.herokuapp.com/hovers",driver,service) 
#kullanıcı kutusu
user = driver.find_element(By.CSS_SELECTOR,"div.figure") 
#kullanıcı ismi
isim = driver.find_element(By.CSS_SELECTOR,"div.figcaption h5") 
#kullanıcı profil linki
link = driver.find_element(By.CSS_SELECTOR,"div.figcaption a")
time.sleep(2)
print(isim.is_displayed())
print("isim:" + isim.text)
time.sleep(2)



#1) Hareket nesnesi oluşturduk:

hareket = ActionChains(driver)
hareket.move_to_element(user) #elementin üstüne fareyi götürür ve sonra click etmek istersek de:
hareket.double_click(user)
hareket.perform()

time.sleep(2)
print("---------")
print(user.is_displayed()) #true vermesi lazımdır. 
print("isim:"+isim.text)
link.click()

#Linki doğrulayalım:
url = driver.current_url
assert "users/1" in url
driver.quit()

