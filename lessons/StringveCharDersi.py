#Yazı Veri Tipleri(String ve Char)
strvar = "python"
print(strvar)
strvar = strvar +" "+"oğren!" 
 #indexler 0 dan başlar.
print(strvar[1:5:2]) #2 den itibaren sona kadar alır.
#[] tek bir eleman alınır.
#[:] başlangıç ve bitiş arasındaki elemanlar alınır. İlk kısım inclusive dir içerir. Son kısım exclusivedir.
#[: :] başlangıç ve bitiş arasındaki elemanlar üçüncü kısımdaki değerlere göre atlayarak alınır.

uzunluk = len(strvar)
print("uzunluk:", uzunluk)
print(strvar * 5)
#UPPER METODU
buyukStrvar = strvar.upper()
print(buyukStrvar) 
#LOWER METODU
kucukStrvar = strvar.lower()
print(kucukStrvar)


#SPLİT METODU:Bir listenin içine her ayrılmış kelimeyi atar.
ayrikStrvar = strvar.split("e")
print(ayrikStrvar) 

print(strvar.encode())