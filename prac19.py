#SEKMELER ARASI GEÇİŞ YAPMA:
import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path="./chromedriver")
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("https://www.apple.com")
time.sleep(3)
print(driver.title)

apple = driver.current_window_handle
#print(driver.current_window_handle) pencerenin handle ını verir.

driver.switch_to.new_window("tab") #Yeni bir sayfa açmak ve yeni bir sekme açmak selenium için aynıdır. Bu yüzden belirtmek gerekir. (tab/window)
driver.get("https://www.tesla.com")

time.sleep(3)
print(driver.title)
tesla = driver.window_handles[1] #ikinci window handle verir.
driver.switch_to.window(apple)
print(driver.title)
time.sleep(2)
driver.switch_to.window(tesla)
print(driver.title)
time.sleep(2)
driver.quit()