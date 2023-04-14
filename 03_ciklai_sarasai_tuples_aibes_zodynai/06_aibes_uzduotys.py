"""
Pirma užduotis
Sukurkite aibę su skaičiais.
Pridėkite skaičių į aibę
Atspausdinkite papildytą aibę.
"""
# aibe = {1, 2, 3, 4, 5, 6, 7, 8}
# aibe.add(69)
# print(aibe)

# pirma_aibe = {1, 2, 3, 4}  # SUGGESTED SOLUTION
# pirma_aibe.add(5)
# print(pirma_aibe)


"""
Antra užduotis
Sukurkite naują aibę su skaičiais.
Ištrinkite skaičių iš aibės.
Atspausdinkite pakoreguotą aibę.
"""
# aibe = {1, 2, 3, 4, 5, 6, 7, 8}
# aibe.remove(7)
# print(aibe)


# antra_aibe = {3, 4, 5, 6, 7, 8}  # SUGGESTED SOLUTION
# antra_aibe.discard(7)
# print(antra_aibe)


"""
Trečia užduotis
Sukurkite naują aibę iš abiejų turimų aibių su tais elementais, kurie yra bendri.
Atspausdinkite naują aibę.
"""
# aibe1 = {1, 2, 3, 4, 5, 6, 7, 8}
# aibe2 = {10, 20, 30, 40, 50, 60, 7, 80}
# aibe3 = aibe1.intersection(aibe2)
# print(aibe3)


# trecia_aibe = pirma_aibe.intersection(antra_aibe)  # SUGGESTED SOLUTION
# print(trecia_aibe)


"""
Ketvirta užduotis
Sukurkite naują aibę iš pirmoje ir antroje užduotyje sukurtų aibių su tais elementais, kurie yra pirmoje aibėje, bet ne antroje.
Atspausdinkite naują aibę.
"""
# aibe1 = {1, 2, 3, 4, 5, 6, 7, 8}
# aibe2 = {10, 20, 30, 40, 50, 60, 7, 80}
# aibe3 = aibe1.difference(aibe2)
# print(aibe3)


# ketvirta_aibe = pirma_aibe.difference(antra_aibe)  # SUGGESTED SOLUTION
# print(ketvirta_aibe)


"""
Penkta užduotis
Sukurkite naują aibę iš pirmoje ir antroje užduotyje sukurtų aibių su tais elementais, kurie yra unikalūs tik antroje.
Atspausdinkite naują aibę.
"""
# aibe1 = {1, 2, 3, 4, 5, 6, 7, 8}
# aibe2 = {10, 20, 30, 40, 50, 60, 7, 80}
# aibe3 = aibe2.difference(aibe1)
# print(aibe3)


# penkta_aibe = antra_aibe.difference(pirma_aibe)  # SUGGESTED SOLUTION
# print(penkta_aibe)


"""
Bonus užduotis
Pakelkite penktosios užduoties aibės elementus kvadratu.
"""
# aibe1 = {1, 2, 3, 4, 5, 6, 7, 8}
# aibe2 = set()
# for element in aibe1:
#     aibe2.add(element**2)
# print(aibe2)


# aibe_kvadratu = {x**2 for x in penkta_aibe}  # SUGGESTED SOLUTION
# print('5 užduoties aibės elementai kvadratu:', aibe_kvadratu)
