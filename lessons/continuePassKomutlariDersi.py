#BREAK DERSİ:
#Bu liste içerisinde c harfinin konumunu öğrenmek istiyorum.
harfler = ["a","b","c","d","e"] * 100
for index, harf in enumerate(harfler):
    if harf == "c":
        print("{}. sırada olan elemanın değeri: {} ".format(index,harf))
        break #yani ilk harfi al ve dur, orda kodu bitir demektir.

#CONTINUE DERSİ:
for sayi in range(1,6):
    if sayi %2 ==  0: #çift sayı demektir.
        continue      #eğer sayı çift sayıysa devam et demek isteriz. tek sayı ise de printleriz.
    print(sayi)

#PASS DERSİ:
for sayi in range(1,6):
    if sayi %2 ==  0: #çift sayı demektir.
        pass      #eğer sayı çift sayıysa geç demek isteriz. else ise yani tek sayı ise de printleriz.
    else:
        print(sayi)
    