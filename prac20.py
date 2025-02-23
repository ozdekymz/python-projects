#BAŞLIK İLE PENCERE DEĞİŞTİRME
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="./chromedriver")
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("https://tomspizzeria.b4a.app/yeni-sekme.html")
time.sleep(3)

facebook = driver.find_element(By.ID, "facebook")
facebook.click()
time.sleep(2)
twitter = driver.find_element(By.ID, "twitter")
twitter.click()
time.sleep(2)
instagram = driver.find_element(By.ID, "instagram")
instagram.click()
time.sleep(2)



time.sleep(2)

def sekmeDegistir(baslik):
    for sayfa in driver.window_handles:    #driver.window_handles ile bir liste alırız. daha sonra handleler içinde tek tek dolaşırız.
        driver.switch_to.window(sayfa)
        if baslik.lower() in driver.title.lower():
            break

sekmeDegistir("facebook")
print("facebook: "+ driver.title)

sekmeDegistir("X")
print("twitter: "+ driver.title)

sekmeDegistir("instagram")
print("instagram: "+ driver.title)

sekmeDegistir("selenium")
print("anasayfa: "+ driver.title)

driver.quit()

























