import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome(executable_path="./chromedriver")
driver.maximize_window()
driver.implicitly_wait(3)
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
button2 = driver.find_element(By.XPATH, "//*[@id='content']/div/ul/li[2]/button")
button2.click()
time.sleep(1)
# Alert beklemek için WebDriverWait kullanın
wait = WebDriverWait(driver, 2)
wait.until(EC.alert_is_present())
time.sleep(1)
# Alert'ı yakalayın
Alert = driver.switch_to.alert
mesaj = Alert.text
time.sleep(1)
# Alert'ı reddedin
Alert.dismiss()
time.sleep(1)
result = driver.find_element(By.ID, "result").text
print("sonuç: "+ result)

print("mesaj: "+mesaj)
driver.quit() 



