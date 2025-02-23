from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from buton.butonaTikla import butonaTikla
from sayfa.sayfaGetirme import sayfaGetir

xpath= "/html/body/div[1]/div[3]/div[2]/div/div/div/div/div/article[2]/div/div/div/div/a[1]"

options = webdriver.ChromeOptions()
options.add_argument('--disable-notifications')
service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service,options=options)
driver.maximize_window()



        
sayfaGetir(driver,"https://www.trendyol.com/","trendyol.com","En Trend Ürünler ")


#css selector/id/xpath en sık kullanılır.
#a ile buton tıklamalarda önemlidir.



butonaTikla(driver,10,By.ID,"onetrust-accept-btn-handler")
butonaTikla(driver,10,By.XPATH,'/html/body/div[1]/div[3]/div[2]/div/div/div/div/div/article[2]/div/div/div/div/a[1]')
butonaTikla(driver,10,By.XPATH,"/html/body/div[1]/div[3]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[4]/div[1]/div/div[1]/div[1]/a")
WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2)) #belirtilen sayfa kadar sayfa açılana kadar bekliyor.
#driver.switch_to.window(driver.window_handles[-1]) #en son elemana gider. ordaki sayfayı tabı açar.
#element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div[5]/main/div/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/div/div/div[1]/h1/span")))
#print(element.text)
#input()

                            
driver.close()



