#WEB DRİVER MANAGER
from baslangic import baslat
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

baslat("https://www.fifa.com/fifaplus/tr",driver)