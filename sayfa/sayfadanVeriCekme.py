
def sayfadanVeriCek(driver,url2,byWhat2,way):
    driver.get(url2)
    seckin_madde_alani = driver.find_element(byWhat2,way)    
    seckin_madde_yazisi = seckin_madde_alani.text 
    seckin_madde_yazisi = seckin_madde_yazisi.split(",")[0]
    print("Seçkin Madde: ", seckin_madde_yazisi)

    """  kaliteli_madde = driver.find_element(By.ID,"mf-tfp").text
    kaliteli_madde = kaliteli_madde.split(",")[0]
    print("Kaliteli Madde:", kaliteli_madde)  """
   
    """ seckin_madde_yazisi = seckin_madde_alani.text 
    seckin_madde_yazisi = seckin_madde_yazisi.split(","),[0] #Stringi istediğimiz yerden split fonksiyonu ile böleriz.
    print("Seçkin Madde: ", seckin_madde_yazisi)
    kaliteli_madde = driver.find_element(By.ID,"mf-tfp").text
    kaliteli_madde = kaliteli_madde.split(","),[0]

    print("Kaliteli Madde:", kaliteli_madde) """



    