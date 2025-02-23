""" #SENKRONİZASYON(BEKLEME): Web sayfaları her zaman çok hızlı yüklenmeyebilir.

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

service = Service("./chromedriver")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://pynishant.github.io/Selenium-python-waits.html")

#1) implicit wait: Gizli bekleme

#driver.implicitly_wait(1) #Bu web driver nesnesi bir sayfada web elementini bulamazsa 20 saniye bekleyecektir. 20 saniye içinde bulamıyorsa hata verir.
#driver nesnesi ile çalışıyor.

#2) explicit wait: Açıktan bekleme
tryIt = driver.find_element(By.XPATH,"//button[contains(text(),'Try it')]")
tryIt.click()


WebDriverWait(driver,45).until(expected_conditions.presence_of_element_located((By.XPATH,"//button[contains(text(),'CLICK ME ')]")))
clickMe = driver.find_element(By.XPATH,"//button[contains(text(),'CLICK ME ')]").click()
driver.quit()



 """

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service("./chromedriver")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://pynishant.github.io/Selenium-python-waits.html")

# 1) implicit wait: Gizli bekleme
# driver.implicitly_wait(1) # Bu web driver nesnesi bir sayfada web elementini bulamazsa 20 saniye bekleyecektir. 20 saniye içinde bulamıyorsa hata verir.
# driver nesnesi ile çalışıyor.

# 2) explicit wait: Açıktan bekleme
tryIt = driver.find_element(By.XPATH, "//button[contains(text(),'Try it')]")
tryIt.click()

""" wait = WebDriverWait(driver, 45)
 """

wait = WebDriverWait(driver, 45)
wait.until(EC.alert_is_present())
driver.switch_to.alert.accept()
wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'CLICK ME ')]"))).click()
#clickMe = driver.find_element(By.XPATH, "//button[contains(text(),'CLICK ME ')]")

#Presence and Visibility:
#Bir element vardır ama kodlarda gözükmüyor olabilir yani visibility demektir bu.
#Sonradan görünür olup olmadığını bulmak istiyorsak visibility kullanırız.



