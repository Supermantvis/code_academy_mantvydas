'''
Pirma užduotis
Sukurkite iteratorių, kuris iteruoja per pateiktą sąrašą ir atspausdina visus lyginius skaičius.
'''
# my_list = [1, 2, 3, 4, 5, 6]

# # Sukuriame iteratoriaus objektą
# my_iterator = iter(my_list)

# # Iteruojame per iteratoriaus elementus su next() metodu
# while True:
#     try:
#         current_number = next(my_iterator)
#     except StopIteration:
#         print("Baigta iteracija")
#         break
#     else:
#         if current_number % 2 == 0:
#             print(current_number)


# SUGGESTED SOLUTION:
# sarasas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for skaicius in sarasas:
#     if skaicius % 2 == 0:
#         print(skaicius)

'''
Antra užduotis
Iteruokite per žodyną, kurio raktai yra raidės, o reikšmės yra skaičiai, ir atspausdinkite tik tas raides, kurių reikšmės yra didesnės nei 4.
'''
# # Sukuriame žodyną
# mano_zodynas = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6}

# # Sukuriame iteratoriaus objektą
# my_iterator = iter(mano_zodynas.items())

# # Iteruojame per iteratoriaus elementus su next() metodu
# while True:
#     try:
#         key, value = next(my_iterator)
#     except StopIteration:
#         print("Baigta iteracija")
#         break
#     else:
#         if value > 4:
#             print(key)


'''
Trečia užduotis
Parašykite programą, kuri naudoja generatorių, generuojantį kiekvieno žodžio ilgį iš teksto.
'''
# zodziai = "Siandien yra labai grazi diena"

# skaidymas = (len(zodis) for zodis in zodziai.split())

# for zodis in skaidymas:
#     print(zodis)


'''
Ketvirta užduotis
Sukurkite generatorių, kuris generuoja visus pirminius skaičius iki nurodyto skaičiaus n.
'''

# def skaiciai_iki_n(num):
#     if num > 1:
#         # check for factors
#         for i in range(2, num):
#             if (num % i) == 0:
#                 yield num


# generatorius = skaiciai_iki_n(100)

# for skaicius in generatorius:
#     print(skaicius)


# SUGGESTED SOLUTION:
def ar_pirminis(skaicius):
    if skaicius < 2:
        return False
    for i in range(2, skaicius):
        if skaicius % i == 0:
            return False
    return True

def pirminiai_iki_n(n):
    for skaicius in range(2, n + 1):
        if ar_pirminis(skaicius):
            yield skaicius

pirminiai_generatorius = pirminiai_iki_n(100)

for skaicius in pirminiai_generatorius:
    print(skaicius)