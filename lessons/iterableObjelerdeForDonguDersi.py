#Diğer iterable objelerde for döngüleri:
""" tup1 = (1,3,5,7)

for sayi in tup1:
    print(sayi) """

liste = [[1,2],[3,4]]
#x ilk haneleri alırken y ikinci haneleri alıyor.
#kaç tane eleman varsa ona göre değişken tanımlamalıyız
""" for x,y in liste: 
    print(x*y) """

kullanici1 = {
    "isim":"Özdenaz",
    "soyad" : "Kaymaz"
}
#print(kullanici1.items())

""" for k,v in kullanici1.items():
    print("Key: {}\t Value: {}".format(k,v)) """

for k in kullanici1.keys():
    print("Key: {}".format(k))