'''
Pirma užduotis
Parašykite funkciją, kuris atspausdina 10 atsitiktinių skaičių nuo 1 iki 100 ir juos išrikiuoja didėjimo tvarka.
'''
# import random

# listas1 = []
# def atsitiktinis_didinimas():
#     for i in range(10):
#         listas1.append(random.randint(1, 100))
#         listas1.sort()
#     return listas1

# print(atsitiktinis_didinimas())

'''
Antra užduotis
Sukurkite kauliukų žaidimą, kuris:

Sugeneruotų tris atsitiktinius skaičius nuo 1 iki 6
Jei vienas iš šių skaičių yra 5, atspausdinti „Pralaimėjai...“
Kitu atveju atspausdinti „Laimėjai!“
Patarimas: Naudoti while ciklą
'''
# import random
# def kauliukai():
#     listas2 = []
#     for i in range(3):
#         listas2.append(random.randint(1, 6))
#     if 5 in listas2:
#         print('pralaimejai')
#     else:
#         print('laimejai')


# kauliukai()


# SUGGESTED SOLUTION:
# print('Bus sugeneruoti 3 skaičiai')
# print('Jei vienas iš jų – 5, tu pralaimėjai!')

# for skaicius in range(3):
#     skaiciai = random.randint(1, 6)
#     print(skaiciai)
#     if skaicius == 5:
#         print('Pralaimėjai...')
#         break
# else:
#     print('Laimėjai!')


'''
Trečia užduotis
Parašykite Python funkciją, kuri priima metus ir mėnesį, o tada atspausdina šio mėnesio kalendorių bei parodo, kiek savaitgalių (šeštadienių ir sekmadienių) yra tame mėnesyje.
'''
import calendar


# def caledoringio(metai, menuo):
#     return calendar.month(metai, menuo)

#     for i in .................................. krc

# print(caledoringio(2023, 4))



# CHATGPT SOLUTION:
# loop through all the months of the year
# for month in range(1, 13):
#     # get the number of days in the month and the day of the week the month starts on
#     days_in_month, starting_day = calendar.monthrange(2023, month)
#     # loop through each day of the month
#     for day in range(1, days_in_month+1):
#         # print the day
#         print(day)


# SUGGESTED SOLUTION:
# def spausdinti_menesio_kalendoriu_ir_savaitgaliu_skaiciu(metai, menesis):
#     print(calendar.month(metai, menesis))

#     _, menesio_ilgis = calendar.monthrange(metai, menesis)  # monthrange output (5, 30)

#     savaitgaliu_skaicius = 0
#     for diena in range(1, menesio_ilgis + 1):
#         savaites_diena = calendar.weekday(metai, menesis, diena)
#         if savaites_diena == 5 or savaites_diena == 6:
#             savaitgaliu_skaicius += 1

#     print(f"Savaitgalių skaičius šiame mėnesyje: {savaitgaliu_skaicius}")

# # Pavyzdys su 2023-ųjų balandžio mėnesiu
# spausdinti_menesio_kalendoriu_ir_savaitgaliu_skaiciu(2023, 4)


# print(calendar.monthrange(2023, 4))
