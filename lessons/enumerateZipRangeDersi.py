#RANGE DERSİ
print(range(10)) #sıfırdan 10 a kadar olan tüm tam sayılar anlamına gelir. 0 dan 9 a kadar
liste = [1,2,3]
newList = list(range(4)) #veya bir diğer yazım tipi
#Broadcasting:
print([*range(10)])
print([*range(2,7,2)])
print(newList) # [0,1,2,3]
#Tipcasting
for sayi in range(10):
    if sayi == 5:
        print(sayi)

#ENUMERATE DERSİ
harfler = ["a","b","c","d","e"]
for index, harf in enumerate(harfler):
    print("{}. sırada olan elemanın değeri: {} ".format(index+1,harf))
#bunların indexlerini bilmek istersek 0 ıncı 1 inci eleman diye enumerate kullanırız.

#ZIP DERSİ
#İki birbiriyle uzunlukları aynı olan listenin birbiri ile eklemlendirilmesini sağlar.
#Uzunluklar farklı ise eleman sayısı az olana göre zipler.
ulkeler = ["TR","FR","DE","USA","UK"] #uzunluğu 3
siralamalar = range(1,5) #uzunluğu 3
for ulke in zip (ulkeler,siralamalar):
    print(ulke) #birleştirilmiş halini gösterir.
