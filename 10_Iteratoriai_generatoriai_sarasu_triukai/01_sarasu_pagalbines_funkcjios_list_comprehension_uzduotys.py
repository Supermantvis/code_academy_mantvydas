# https://github.com/infohata/course-python-basic/blob/main/10_Iteratoriai_generatoriai_sarasu_triukai/01_sarasu_pagalbines_funkcjios_list_comprehension.md
# https://github.com/infohata/course-python-basic/blob/main/PTU12_live/list_comprehension.ipynb
'''
Pirma užduotis
Sukurkite programą, kuri naudoja lambda, map() ir filter() funkcijas, kad atrinktų sąrašo elementus, didesnius už 10, ir padidintų juos dvigubai. Palyginkite šį rezultatą su tuo, ką gautumėte naudodami "list comprehension".
'''
# sarasas = [1, 2, 3, 4, 50]

# # daugiau_uz_10 = map(lambda x: x * 2, filter(lambda x: x > 10, sarasas))
# # print(list(daugiau_uz_10))

# padvigubinta = [skaicius * 2 for skaicius in sarasas if skaicius > 10]
# print(padvigubinta)


# # SUGGESTED SOLUTION:
# sarasas = [5, 12, 7, 18, 4, 15]

# # Atrinkti ir padidinti dvigubai skaičius, didesnius už 10
# result = map(lambda x: x * 2, filter(lambda x: x > 10, sarasas))
# print(list(result))  # [24, 36, 30]

# # Su paprastomis funkcijomis ir `for` ciklais
# result = [x * 2 for x in sarasas if x > 10]
# print(result)  # [24, 36, 30]


'''
Antra užduotis
Parašykite programą, kuri naudoja reduce() funkciją, kad rastų sąrašo elementų sandaugą.
'''

# from functools import reduce

# sarasas = [1, 2, 3, 4, 5]
# sandauga = reduce(lambda x, y: x * y, sarasas)
# print(sandauga)


'''
Trečia užduotis
Naudodamiesi statistics moduliu, apskaičiuokite ir išveskite sąrašo elementų sumą, vidurkį, medianą, mažiausią ir didžiausią elementą.
'''
# import statistics

# sarasas = [1, 2, 3, 4, 5]
# print(sum(sarasas))  # sumą
# print(statistics.mean(sarasas))  # vidurkį
# print(statistics.median(sarasas))  # medianą
# print(min(sarasas))  # mažiausią
# print(max(sarasas))  # didžiausią


'''
Ketvirta užduotis
Sukurkite programą, kuri naudoja sort() arba sorted() funkcijas, kad rūšiuotų sąrašą skaičių pagal jų liekanas dalinant iš 3 (atsižvelgiant į key parametrą).
'''
# sarasas = [30, 90, 60, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# rusiuotas_sarasas = sorted(sarasas, key=lambda x: x % 3 == 0)
# print(rusiuotas_sarasas)


# SUGGESTED SOLUTION:
# sarasas = [3, 1, 4, 1, 5, 9, 2]

# result = sorted(sarasas, key=lambda x: x % 3)
# print(result)  # [3, 9, 1, 4, 1, 5, 2]


'''
Penkta užduotis
Sukurkite programą, kuri naudoja lambda, filter() ir reduce() funkcijas, kad apskaičiuotų vidurkį tų sąrašo skaičių, kurie yra lyginiai. Palyginkite šį rezultatą su tuo, ką gautumėte naudodami "list comprehension".
'''
from functools import reduce
import statistics

# REIK PABAIGT!!!!!!!!!!!!!!!!!!!
sarasas = [1, 2, 3, 4, 50, 10, 11, 16]

lyginiai = map(lambda x: x * 2, filter(lambda x: x > 10, sarasas))
