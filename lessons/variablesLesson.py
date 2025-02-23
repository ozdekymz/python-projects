#variable = a container for a value.
first_name = "Bro"
last_name = "Code"
full_name = first_name +" " +last_name
print(full_name)
""" print(type(name))
print("hello "+ name) """

#\n new line yani yeni bir satır demektir. \t ise tab bırakır.
#Dinamik ve Statik Farkı:
#Format ne demek: Süslü prantezin içini doldurmamız gereken ifadeyi formata atıyoruz.
print("Benim adım {}".format('Mesut'))
print("Benim adım {}, yaşım {}".format('Mesut',32))
print("Benim adım {first_name}, yaşım {age}".format(first_name='Mesut',age=32))
