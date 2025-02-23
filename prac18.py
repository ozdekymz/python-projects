#YENİ BİR SEKME AÇMA:
import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path="./chromedriver")
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("https://www.apple.com")
time.sleep(3)
driver.switch_to.new_window("window") #Yeni bir sayfa açmak ve yeni bir sekme açmak selenium için aynıdır. Bu yüzden belirtmek gerekir. (tab/window)
driver.get("https://www.tesla.com")
time.sleep(3)
driver.quit()
