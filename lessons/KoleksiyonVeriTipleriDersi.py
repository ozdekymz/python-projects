#List ve Set
liste = ["a","b","c","d","e","a"]

print("Örnek 1:")
liste = liste + ["f"]
print(liste[3:5])

print("Örnek 2:")
liste3 = liste.pop(-2)
print(liste3)

print("Örnek 3:")
liste.append("g") #atama gerektirmeyen yani listeye eşitlemeye gerek kalmayan komutlar vardır
print(liste)
#sayilar.sort() #azdan çoka sıralar.
#sayilar.reverse() #tersine döndürür sıralar.

sayilar = [1,2,3,4,5,4,3,2]
print(set(sayilar)) #mükerrer ifadeleri önler.
print(sayilar.count(2)) #2 den kaç tane var saydırırız.
