#SAYFAYI AŞAĞI VE YUKARI KAYDIRMA:
#driver.execute_script ile bir javascript fonk. kullanmamız mümkündür.
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service = Service("./chromedriver")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://www.homeexchange.com/")

#driver.execute_script("window.scrollBy(0,300)","")

acceptButton= driver.find_element(By.ID,"onetrust-accept-btn-handler")
acceptButton.click()
time.sleep(3)
#İstediğimiz kelimeyi aratarak oraya kadar inmek istersek(Web element kullanarak):
kelime = driver.find_element(By.XPATH,"//*[@id='how-it-works']/div/div/div/footer/button")
#Bu web elementi bulana kadar sayfanın altına inmesini istersek:
driver.execute_script("arguments[0].scrollIntoView()",kelime)
time.sleep(2)
driver.execute_script("window.scrollBy(0,-200)","")
#Sana verilen argüman görünür olana kadar scroll yap demektir.
input()





""" driver.execute_script("window.scrollBy(0,300)")
time.sleep(3)
driver.execute_script("window.scrollBy(0,3000)")
time.sleep(5) """


""" #Sayfanın en altına inmek istersek:
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
input() """

 




""" driver.execute_script("window.scrollBy(0,200)", "") 
#Burda sayfayı aşağı kaydırmak istedik. Window o anki chrome penceresidir.
#(0 dan yani bulunduğumuz noktadan 150 px kaydırmak istiyoruz.)

time.sleep(2)
driver.execute_script("window.scrollBy(0,-150)", "") 
#- numara verirsek de yukarı kaydırmış oluruz.
driver.save_screenshot("./sonuc1.png")
driver.quit() """