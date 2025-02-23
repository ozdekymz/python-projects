#Veri Tipleri ve Sayı Tipleri: (Data Types) 
#type() değişkeni kullanarak sorgulanabilir.
#Integer(int) -- sayı
#Float(float) -- ondalıklı sayı
#String(str) -- yazı
#Boolean(bool) -- mantıki ifadeler/mantıki sorgulamalar yaparken kullanılır. (true,false)
#List(list) -- [1,2,True,a,1] her veri tipini içinde barındırır.
#Set(set) -- {1,2,3,4,3} == {1,2,3,4} listten tek farkı duplicate verileri önlüyor.Birden fazla tekrar eden verileri bulur ve teke indirir. 
#Dictionary(dict) -- {"isim" : Mesut, "yas": 32 } key ve isimden oluşur. Boyutlardan oluşur.
#Tuple(tup) -- (1,2,True) -- Birden fazla değer tutmaya yarayan fakat değiştirilemeyen veri tipidir.
""" 
element = [1,2,"özde","deneme",0.5]
tip = type(element)
print(tip)
input()
element2 = {1,"ozde",1,2,3}
print(element2)
input()
element = {"isim" : "Özde", "Yas": 32}
tip = type(element)
print(tip)
input()
print(5%3)

sayi = 5
print(type(sayi))

sayi2 = 5.2
print(type(sayi2))
"""
insanlar = [
    ["Özde",23],
    ["Ali",46],
    ["Sinem",38]

]
for insan in insanlar:
    for isim,yas in insan:
        if isim == "Sinem":
            print(isim,yas)
        
    
#insanlar arrayinin içinden sinem adındaki değeri bulan kodu yaz

for isim, yas in insanlar:
    if isim == "Sinem":
        print(isim, yas)








