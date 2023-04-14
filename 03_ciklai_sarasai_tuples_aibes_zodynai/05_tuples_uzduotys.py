"""
Pirma užduotis
Sukurkite tuple, kuris susideda iš jūsų mėgstamų grupių pavadinimų.
Atspausdinkite tuple.
"""
# grupes = ('worakls', 'nto', 'some other band')
# print(grupes)

# megstamos_grupes = ('Radiohead', 'The Beatles', 'Pink Floyd', 'Led Zeppelin')  # SUGGESTED SOLUTION
# print(megstamos_grupes)


"""
Antra užduotis
Sukurkite dar vieną tuple su grupių pavadinimais (pavadinimai gali kartotis) ir sujunkite abu turimus tuple į vieną naują.
Atspausdinkite naują tuple.
"""
# grupes = ('worakls', 'nto', 'some other band')
# grupes2 = ('linkin park', 'shrek pop', 'teletubies')
# grupes_sum = grupes + grupes2
# print(grupes_sum)


# kitos_grupes = ('Queen', 'The Beatles', 'Nirvana', 'Led Zeppelin')  # SUGGESTED SOLUTION
# visos_grupes = megstamos_grupes + kitos_grupes
# print(visos_grupes)

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


# print(visos_grupes[0])  # SUGGESTED SOLUTION
# print(visos_grupes[2])
# print(visos_grupes[-1])

"""
Ketvirta užduotis
Atspausdinkite kas antrą grupę.
"""
# grupes = ('worakls', 'nto', 'some other band 1', 'some other band 2')
# print(grupes[::2])


# print(visos_grupes[::2])  # SUGGESTED SOLUTION


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


# kartai = visos_grupes.count('Led Zeppelin')  # SUGGESTED SOLUTION
# print("Grupė 'Led Zeppelin' pasikartoja: ", kartai)

# indeksas = visos_grupes.index('Pink Floyd')
# print("Grupės 'Pink Floyd' indeksas yra: ", indeksas)

# print('Deep Purple' in visos_grupes)


"""
Bonus užduotis
Atspausdinkite grupes atskirose eilutėse taip, kad pavadinimai nesidubliuotų.
"""
# grupes = ('worakls', 'worakls', 'nto', 'christian loffler', 'some other band 1')
# for grupe in set(grupes):
#     print(grupe)


# unikalios_grupes = tuple(set(visos_grupes))  # SUGGESTED SOLUTION

# for grupe in unikalios_grupes:
#   print(grupe)