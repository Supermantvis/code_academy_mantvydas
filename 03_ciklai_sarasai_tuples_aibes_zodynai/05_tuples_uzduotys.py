"""
Pirma užduotis
Sukurkite tuple, kuris susideda iš jūsų mėgstamų grupių pavadinimų.
Atspausdinkite tuple.
"""
# grupes = ('worakls', 'nto', 'some other band')
# print(grupes)


"""
Antra užduotis
Sukurkite dar vieną tuple su grupių pavadinimais (pavadinimai gali kartotis) ir sujunkite abu turimus tuple į vieną naują.
Atspausdinkite naują tuple.
"""
# grupes = ('worakls', 'nto', 'some other band')
# grupes2 = ('linkin park', 'shrek pop', 'teletubies')
# grupes_sum = grupes + grupes2
# print(grupes_sum)


"""
Trečia užduotis
Atspausdinkite pirmą grupę.
Atspausdinkite trečia grupę.
Atspausdinkite paskutinę grupę.
"""
# grupes = ('worakls', 'nto', 'some other band 1', 'some other band 2')
# print(grupes[0])
# print(grupes[2])
# print(grupes[-1])


"""
Ketvirta užduotis
Atspausdinkite kas antrą grupę.
"""
# grupes = ('worakls', 'nto', 'some other band 1', 'some other band 2')
# print(grupes[::2])


"""
Penkta užduotis
Atspausdinkite kiek kartų sąraše kartojasi kuri nors grupė.
Atspausdinkite kurios nors grupės indeksą.
Patikrinkite ar kuri nors grupė yra tuple.
"""
# grupes = ('worakls', 'worakls', 'nto', ('some other band 1', 'some other band 2'))
# print('part 1: ', grupes.count('worakls'))
# print('part 2: ', grupes.index('worakls'))
# print('part 3: ', type(grupes[3]))


"""
Bonus užduotis
Atspausdinkite grupes atskirose eilutėse taip, kad pavadinimai nesidubliuotų.
"""
# grupes = ('worakls', 'worakls', 'nto', 'christian loffler', 'some other band 1')
# for grupe in set(grupes):
#     print(grupe)