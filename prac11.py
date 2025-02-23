#STATİK DROPDOWN LİST

#select tagi html de dropdown menu oluşturmak için kullanılır.
#option tagi de bu seçenekleri belirlemek için kullanılır.
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://tomspizzeria.b4a.app/")
dropdown = driver.find_element(By.ID,"odeme-tipi") #web elemente koyduk.
odeme = Select(dropdown) #select classı
# Eğer dropdown çoklu seçim özelliğine sahipse
if odeme.is_multiple:
    print("Bu dropdown çoklu seçim yapılabilir.")
else:
    print("Bu dropdown yalnızca tek bir seçenek seçmenize izin verir.")


#Seçenekleri alır ve yazdırır:

""" odeme_tipleri = odeme.options #web element listesi her bir option tagi için.
for tip in odeme_tipleri:
    print(tip.text)  """
time.sleep(2)
odeme.select_by_visible_text("Kredi Kartı") #hangi optionu seçmek isteriz bunu belirler.
time.sleep(2)
odeme.select_by_index("3") #sıra numarasını vererek seçim işlemini gerçekleştiririz.
#3odeme.first_selected_option() #ilk sırada ne varsa onu seçer
#odeme.is_multiple : Birden fazla opsiyon seçilebiliyor mu bunun true false döndürür.
#deselect_by_index : Kaldırmak istediğimiz seçeneğin indexini verebiliriz. Seçilileri kaldırmak için kullanılır.