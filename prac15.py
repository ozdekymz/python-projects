import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions 
from selenium.webdriver.common.alert import Alert

service = Service("./chromedriver")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://pynishant.github.io/Selenium-python-waits.html")

tryIt = driver.find_element(By.XPATH, "//button[contains(text(),'Try it')]")
tryIt.click()

WebDriverWait(driver, 45).until(expected_conditions.presence_of_element_located((By.XPATH, "//button[contains(text(), 'CLICK ME')]")))
clickme = driver.find_element(By.XPATH, "//button[contains(text(), 'CLICK ME')]").click()


#KISACASI ALERT ÇIKINCA KAPATMAK İSTERSEK:

WebDriverWait(driver,3).until(expected_conditions.alert_is_present()) #Burda bir js uyarısı görünene kadar bekle.
uyari = Alert(driver)
time.sleep(1)
uyari.accept()






