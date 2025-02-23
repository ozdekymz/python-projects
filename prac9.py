#WEB ELEMENT LİSTESİ: Birden fazla elementle çalışmamız gerekirse ne yapmalıyız?
#***
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
#***
from buton.butonaTikla import butonaTikla


service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window() 
#senaryomuz:
#menuye tıklanacak.
#top 250 moviese tıklanacak.
#listedeki tüm elemanları çek.

driver.get("https://www.imdb.com/")
butonaTikla(driver,10,By.ID,"imdbHeader-navDrawerOpen") #labeldan id çektik.
butonaTikla(driver,10,By.XPATH,"//span[text()='Top 250 Movies']")
""" film_isimleri = driver.find_elements(By.XPATH,"//div[@id='__next']/main/div/div[3]/section/div/div[2]/div/ul/li/div[2]/div/div/div/a") """
""" moviesLIs = WebDriverWait(driver,10).until(

        EC.presence_of_all_elements_located((By.XPATH, '//ul[@class="ipc-metadata-list ipc-metadata-list--dividers-between sc-3f13560f-0 sTTRj compact-list-view ipc-metadata-list--base"]/li')))




for i in moviesLIs:
    print(i.find_element_by_xpath(".//h3").text) """
film_tarih = driver.find_elements(By.XPATH,"//*[@id='__next']/main/div/div[3]/section/div/div[2]/div/ul/li/div[2]/div/div/div[2]/span[1]")
film_isim = driver.find_elements(By.XPATH,"//div[@id='__next']/main/div/div[3]/section/div/div[2]/div/ul/li/div[2]/div/div/div/a")


""" for i in range(20):
    print(film_isimleri[i].text) """

""" for i in film_tarih:
    if i.text == "2000":
        print(i.text)

driver.quit()  """

for i in range(len(film_tarih)):
    if film_tarih[i].text == "2000":
        film_adi = film_isim[i].text
        print(f"Film Adı: {film_adi}")

    
    

#find_element() --> o sorguya uyan ilk web elementi karşımıza getirir.
#find_elements() --> bize bir liste halinde döndürür.
