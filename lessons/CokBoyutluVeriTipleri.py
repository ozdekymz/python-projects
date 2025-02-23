#Dictionary:
dict1 = {"isim": "Mesut","yas": 32,"lokasyon" : "Berlin"}
#veya bu tarz yazılabilir.
dict1 = {
    "isim" : "Mesut",
    "yas"  : 32,
    "dogdugu_sehir" : "İzmir",
    "yasadigi_sehir" : "Berlin",
    }
dict2 = {
    "isim" : "Mesut",
    "yas"  : 32,
    "lokasyon" : {
        "dogdugu_sehir" : "İzmir",
        "yasadigi_sehir" : "Berlin",
    }
    }
print(dict1.get("yas"))
print(dict2["lokasyon"]["yasadigi_sehir"]) #veya print(dict2.get("lokasyon").get("yasadigi_sehir"))
#dic içinde dic de eklenebilir.

#Get Metodu
print(dict2.get("lokasyon").get("yasadigi_sehir"))

#Keys Metodu
print(dict2.keys())

#Values:
print(dict1.values())
#items:
print(dict2.items())
