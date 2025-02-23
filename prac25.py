#DİNAMİK DROPDOWN
import time
from baslangic import baslat
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver import ActionChains


service = Service("./chromedriver")
driver = webdriver.Chrome(service=service)

baslat("https://www.ucuzabilet.com",driver,service)
time.sleep(3)
driver.execute_script("document.getElementsByTagName('efilli-layout-etstur')[0].style.display='none';") #js kodu entegre ettik.
#/html/body/efilli-layout-etstur//div/div[4]

#//li[contains=(text(),'GRZ')

nereden = driver.find_element(By.ID,"from_text")
nereden.send_keys("avust")
time.sleep(2)
graz = driver.find_element(By.XPATH,"//*[@id='ui-id-7']/li[6]")
graz.click()
time.sleep(2)
driver.quit()



