import time
from selenium.webdriver.common.by import By #id import ettik. 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from buton.butonaTikla import butonaTikla
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from inputGirme import inputGir

service = Service(executable_path='./chromedriver.exe')
#options = webdriver.ChromeOptions()
#options.add_argument("--headless=new")
#driver = webdriver.Chrome(service=service, options=options)
driver = webdriver.Chrome(service=service)
driver.maximize_window()



#Yanlış Kullanıcı Adı Girince:

driver.get("https://the-internet.herokuapp.com/login")
inputGir(driver,10,By.ID,"username","tom")
inputGir(driver,10,By.ID,"password","SuperSecretPassword!")
butonaTikla(driver,10,By.XPATH,"/html/body/div[2]/div/div/form/button")
mesaj = driver.find_element(By.ID,"flash").text

if "Your username is invalid!" in mesaj:
    print("OK, Yanlış kullanıcı adı doğru çalışıyor.")
else:
    print("HATA: Yanlış kullanıcı adı çalışmıyor.")

#Yanlış Şifre Girince:
driver.get("https://the-internet.herokuapp.com/login")
inputGir(driver,10,By.ID,"username","tomsmith")
inputGir(driver,10,By.ID,"password","Super")
butonaTikla(driver,10,By.XPATH,"/html/body/div[2]/div/div/form/button")
mesaj2 = driver.find_element(By.ID,"flash").text

if "Your password is invalid!" in mesaj2:
    print("OK, Yanlış şifre doğru çalışıyor.")
else:
    print("HATA: Yanlış şifre çalışmıyor.")


#İkisini de doğru girince:
driver.get("https://the-internet.herokuapp.com/login")
inputGir(driver,10,By.ID,"username","tomsmith")
inputGir(driver,10,By.ID,"password","SuperSecretPassword!")
butonaTikla(driver,10,By.XPATH,"/html/body/div[2]/div/div/form/button")
mesaj = driver.find_element(By.ID,"flash").text

if "You logged into a secure area!" in mesaj:
    print("OK, Doğru bilgiler doğru çalışıyor.")
else:
    print("HATA: Doğru bilgiler çalışmıyor.")

linkimiz = driver.current_url

if "secure" in linkimiz:
    print("OK. Link secure içeriyor.")
else:
    print("HATA: Link secure içermiyor.")

dogru_mesaj = driver.find_element(By.XPATH,"//*[@id='content']/div/h4").text
if "Secure Area" in dogru_mesaj:
    print("OK. Sayfa başlığı doğru.")
else:
    print("HATA: Sayfa başlığı yanlış.")


#Logout butonuna tıklanır.
butonaTikla(driver,10,By.XPATH,"//*[@id='content']/div/a")
#Sayfa linkini doğrularız.
if "login" in driver.current_url:
    print("OK. Login sayfasına döndük.")

else:
    print("HATA: Login sayfasına dönmedi.")
    driver.save_screenshot("./ekrangoruntusu3.png")

driver.quit()





#istenileni yapıyor mu(pozitif test)
#istenmeyeni yapmıyor mu(negatif test)

#Adım 1: İnternet login sayfasına git. https://the-internet.herokuapp.com/login
#Adım 2:Kullanıcı adı girilir.
#Adım 3: Şifre girilir.
#Adım 4: Login butonuna tıkla.

#Yanlış kullanıcı adında ->  Your username is invalid! mesajı görülmelidir.
#Yanlış parola girilirse -> Your password is invalid! mesajı görülmelidir.
#İkisi de doğru girilirse -> You logged into a secure area! mesaji görülür. Link secure olacaktır. Sayfada secure area yazıcaktır.

#Refactoring: Yazılmış kodu optimize etme.Var olan kod içinde fazla olan kısımları çıkartarak satır sayısını azaltma.