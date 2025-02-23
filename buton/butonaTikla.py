from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def butonaTikla(driver,timeWait,byWhat,way):
    element = WebDriverWait(driver, timeWait).until(EC.element_to_be_clickable((byWhat,way))) #elementi aldı elementin içinde şuan
    element.click()
    