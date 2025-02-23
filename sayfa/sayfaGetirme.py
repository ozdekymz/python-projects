
def sayfaGetir(driver,url,word,baslik2):
    driver.get(url)
    link = driver.current_url
    baslik = driver.title #şuanki başlığı getirir.    
    print("baslik:"+ baslik)
    if word in link:
        print("Doğru "+ baslik2 + "Sayfasındayız:"+link)
    else:
        driver.save_screenshot("./ekrangoruntusu2.png") #doğru sayfada değilsek screenshot almasını isteriz. Testin fail verdiği durumlarda kullanılır.