#RADIO DÜĞMESİ VE CHECKBOX

#Radio düğmesi: Kullanıcıya birden fazla seçenek sunulup bir tanesinin işaretlenmesi istendiğinde kullanılır.
#Check Box: Kullanıcının birden fazla seçeneği işaretlemesi istenilen durumlarda kullanılır.

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from buton.butonaTikla import butonaTikla
from selenium.webdriver.support.select import Select



service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://tomspizzeria.b4a.app/")
""" orta_boy = butonaTikla(driver,10,By.CSS_SELECTOR,"input[value='Orta']")
print(orta_boy.is_selected())
orta_boy = driver.find_element(By.CSS_SELECTOR,"input[value='Orta']")
butonaTikla(driver,10,By.CSS_SELECTOR,"input[value='Orta']")
print(orta_boy.is_selected()) """
zeytin = driver.find_element(By.CSS_SELECTOR,"input[value='zeytin']")
butonaTikla(driver,10,By.CSS_SELECTOR,"input[value='zeytin']")
print(zeytin.is_selected())
mantar = butonaTikla(driver,10,By.CSS_SELECTOR,"input[value='mantar'")




#is_selected -- radio düğmesi veya checkbox seçili mi bunu öğrenmek için kullanırız.
#is_enabled -- şuan aktif mi değil mi mesela buton için kullanılır. 








#is_selected -- radio düğmesi veya checkbox seçili mi bunu öğrenmek için kullanırız.
#is_enabled -- şuan aktif mi değil mi mesela buton için kullanılır. 



