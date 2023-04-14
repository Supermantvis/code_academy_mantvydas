"""
Pirma užduotis
Sukurkite sąrašą su bent penkiais elementais
Atspausdinkite jį naudodami for ciklą
"""
# skaiciai = [1, 2, 3, 4, 5]
# for skaicius in skaiciai:
#     print(skaicius)


"""
Antra užduotis
Sukurti programą, kuri:

Leistų vartotojui po vieną įvesti 5 žodžius
Pridėtų įvestus žodžius į sąrašą
Atspausdintų kiekvieną žodį, jo ilgį ir eilės numerį sąraše (nuo 1)
Iššūkis 💡: padarykite, kad programa leistų įvesti norimą žodžių kiekį
Patarimas: Naudoti sąrašą (list), ciklą for, funkcijas len ir index
"""
# sarasas = []
# norimas_zodziu_kiekis = int(input("Iveskite įvesti norimą žodžių kiekį: "))
# for i in range(0, norimas_zodziu_kiekis):
#     a = sarasas.append(input("Iveskite savo zodi: "))


# for indeksas, reiksme in enumerate(sarasas):
#     print(indeksas, reiksme, "ilgis: ", len(reiksme))


"""
Trečia užduotis
Sukurti programą, kuri:

Leistų vartotojui įvesti metus
Atspausdintų "Keliamieji metai", jei taip yra
Atspausdintų "Nekeliamieji metai", jei taip yra
"""
# sarasas = []
# for i in range(0, 5):
#     sarasas.append(input("Iveskite metus nuo 2000 iki 2005: "))
#     if sarasas[i] == '2003':
#         print(sarasas[i], ' yra Keliamieji metai')
#     else:
#         print(sarasas[i], ' yra Nekeliamieji metai')


"""
Ketvirta užduotis
Perdaryti trečią užduoti taip, kad programa atspausdintų visus keliamuosius metus, nuo 1900 iki 2100 metų.
"""
# for i in range(1900, 2100):
#     if (i % 4) == 0:
#         print(i, ' yra Keliamieji metai')
#     else:
#         print(i, ' yra Nekeliamieji metai')