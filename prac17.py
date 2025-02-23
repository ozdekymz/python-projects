#BİR JS UYARISI BİZDEN METİN GİRMEMİZİ İSTEYEBİLİR:
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert


driver = webdriver.Chrome(executable_path="./chromedriver")
driver.maximize_window()
driver.implicitly_wait(3)
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
button2 = driver.find_element(By.XPATH, "//*[@id='content']/div/ul/li[3]/button")
button2.click()
time.sleep(1)

# Alert beklemek için WebDriverWait kullanın.
wait = WebDriverWait(driver, 2)
wait.until(EC.alert_is_present())
time.sleep(1)
# Alert'ı tanımlayın.
alert = Alert(driver)

mesaj = alert.text
time.sleep(1)
# Alerte input girin.
alert.send_keys("I am happy!")
#Alerti onaylayın.
alert.accept()
time.sleep(1)
result = driver.find_element(By.ID, "result").text
print("sonuç: "+ result)
