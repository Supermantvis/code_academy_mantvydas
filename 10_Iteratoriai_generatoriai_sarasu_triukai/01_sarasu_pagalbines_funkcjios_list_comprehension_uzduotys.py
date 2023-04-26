# https://github.com/infohata/course-python-basic/blob/main/10_Iteratoriai_generatoriai_sarasu_triukai/01_sarasu_pagalbines_funkcjios_list_comprehension.md
# https://github.com/infohata/course-python-basic/blob/main/PTU12_live/list_comprehension.ipynb
'''
Pirma užduotis
Sukurkite programą, kuri naudoja lambda, map() ir filter() funkcijas, kad atrinktų sąrašo elementus, didesnius už 10, ir padidintų juos dvigubai. Palyginkite šį rezultatą su tuo, ką gautumėte naudodami "list comprehension".
'''
sarasas = [1, 2, 3, 4, 5]
rezultatas = map(lambda x: x ** 2, sarasas)
print(list(rezultatas))  # [1, 4, 9, 16, 25]

def kvadratas(x):
    return x ** 2

rezultatas = map(kvadratas, sarasas)
print(list(rezultatas))  # [1, 4, 9, 16, 25]