'''
Pirma užduotis
Sukurkite anoniminę funkciją, kuri iš sąrašo skaičių pasirenka tik tuos, kurie yra didesni nei 10.
'''

daugiau = iter(lambda x: x>10, [1, 2, 3, 4, 5, 11, 20, 30, 50])


skaiciai = [1, 20, 3, 40, 5, 60, 7, 80, 9, 100]
didziau_nei_10 = list(filter(lambda x: x > 10, skaiciai))
print(didziau_nei_10) # išveda [20, 40, 60, 80, 100]

'''
Antra užduotis
Sukurkite anoniminę funkciją, kuri grąžina sąrašo elementų vidurkį.
'''

# listas = list(avg(lambda x: [1, 2, 3, 4, 5, 11, 20, 30, 50]))

# skaiciai = [1, 2, 3, 4, 5]
# vidurkis = lambda x: sum(x) / len(x)

# print(vidurkis(skaiciai)) # išveda 3.0


'''
Trečia užduotis
Parašykite anoniminę funkciją, kuri grąžina didžiausią skaičių iš duotų trijų skaičių.
'''

