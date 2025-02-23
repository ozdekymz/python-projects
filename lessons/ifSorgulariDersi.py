""" print("Örnek 1")
hava_durumu = "sicak"

if hava_durumu ==   "karli":
    print("Şemsiyeni al!")
elif hava_durumu == "sicak":
    print("atkını al")
else:
    print("Sorun yok")

print("Örnek 2")
liste = ["a","b","c"]

hedef_harf = "d"
if hedef_harf in liste:
    print("var")
else:
    print("mevcut değil")
    
print("Örnek 3:")
liste = ["a","b","c"]

hedef_harf = "e"
if hedef_harf in liste:
    print("var")
else:
    print("mevcut değil, yenisi ekleniyor..")
    liste.append("d")
    print("güncel liste: {}".format(liste)) #süslü parantezin içini liste ile dolduruyoruz. """

print("Örnek 3:")
liste = ["a","b","c"]

hedef_harf = "e"
if (hedef_harf in liste) and (hedef_harf) == liste[0]: #iki koşullu durumu birbirine bağladık.
    print("var ve ilk harf konumunda")
elif (hedef_harf in liste):
    print("var ama ilk harf değildir.")
else:
    print("mevcut değil, yenisi ekleniyor..")
    liste.append("d")
    print("güncel liste: {}".format(liste)) #süslü parantezin içini liste ile dolduruyoruz.


    

