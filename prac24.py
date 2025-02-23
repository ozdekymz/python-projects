#FARE İLE SÜRÜKLE BIRAK --  DRAG AND DROP
import time
from baslangic import baslat
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

service = Service("./chromedriver")
driver = webdriver.Chrome(service=service)

baslat("https://demoqa.com/droppable/",driver,service)
source = driver.find_element(By.ID,"draggable")
target = driver.find_element(By.ID,"droppable")

print("Önce: " + source.text)

action = ActionChains(driver)
action.drag_and_drop(source,target) #source ve target adında iki parametre ister.



action.perform() #Bunu koymazsak harekete geçmez.
#action.context_click yaparsak farenin sağ tarafına tıklamaktır. Elementin üstünde sağ tıklayabiliriz.
print("Sonra:" + target.text)
driver.quit()

