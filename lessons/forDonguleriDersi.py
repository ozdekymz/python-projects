#Kullanım Yapısı:
#for <degisken> in <iterable>
#<buraya yazılanı yap.>

#for / in ve : kullanımı önemlidir.
""" for kullanici in yorum_birakanlar:
    print(kullanici) 

kullanici_sayisi = 0
for kullanici in yorum_birakanlar:
    kullanici_sayisi = kullanici_sayisi + 1 #ya da kullanici_sayisi += 1
    
ad, soyad = kullanici.split()[0], kullanici.split()[1]
print("{0}.Kullanici Adi {1} ve Soyadi {2}".format(kullanici_sayisi,ad,soyad)) """


yorum_birakanlar=["Özde Kaymaz","Ali Bayram","Uğuray Eray","Gizem Yılmaz","Ceren Yılmaz","Selen Yılmaz","Ferhat Ibrik"]
moderator = "Ferhat Ibrik"

kullanici_sayisi = 0
moderator_sayisi = 0

for kullanici in yorum_birakanlar:
    kullanici_sayisi += 1
    ad,soyad = kullanici.split()[0], kullanici.split()[1]
    

    if (kullanici == moderator):
        moderator_sayisi +=1 #moderator_sayisi = moderator_sayisi + 1
        print("{0}. Moderatörün Adı {1} ve Soyadi {2}.".format(moderator_sayisi,ad, soyad))

    else:
        kullanici_sayisi += 1
        print("{0}. Kullanıcının Adı {1} ve Soyadi {2}.".format(kullanici_sayisi,ad, soyad))
    
    
        



