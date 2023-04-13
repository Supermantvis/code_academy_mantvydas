"""
Pirma uzduotis:
Sukurkite sąrašą su bent penkiais jūsų mėgstamų maisto produktų pavadinimais.
Atspausdinkite visą sąrašą.
"""
# sarasas = ['obuolys', 'bananas', 'kriause', 'melionas', 'alus']
# print(sarasas)


"""
Antra uzduotis:
Atspausdinkite sąrašo pirmą elementą.
Atspausdinkite sąrašo trečią elementą.
Atspausdinkite sąrašo paskutinį elementą.
"""
# sarasas = ['obuolys', 'bananas', 'kriause', 'melionas', 'alus']
# print(sarasas[0])
# print(sarasas[2])
# print(sarasas[-1])


"""
Trecia uzduotis:
Atspausdinkite sąrašo pirmus tris elementus.
Atspausdinkite sąrašo paskutinius du elementus.
Atspausdinkite tris elementus iš sąrašo vidurio.
Atspausdinkite sąrašo kas antrą elementą.
"""
# sarasas = ['obuolys', 'bananas', 'kriause', 'melionas', 'alus']
# print(sarasas[:-2])
# print(sarasas[2:])
# print(sarasas[::2])


"""
Ketvirta uzduotis:
Pridėkite dar vieną mėgstamo maisto pavadinimą į sąrašo galą. 1+ 
Įterpkite naują maisto produktą į sąrašo ketvirtą vietą. 2+ 
Pakeiskite antrąjį sąrašo elementą kitu mėgstamo maisto pavadinimu. 3+
Ištrinkite pirmąjį sąrašo elementą. 4+
Ištrinkite sąrašo trečią elementą. 5+
Suraskite sąraše kurio nors elemento indeksą. 6+
Atspausdinkite sąrašą atvirkštine tvarka. 7+
Pabandykite papildomai panaudoti kitus metodus. 8+
"""
# sarasas = ['obuolys', 'bananas', 'kriause', 'melionas', 'alus']
# print('\npradinis sarasas: ', sarasas)

# sarasas.append('pienas') # 1
# print('\n1. uzt. pridetas elementas: \'pienas\':', sarasas)

# sarasas.insert(3, 'kivi') # 2
# print('\n2. uzd. iterptas 4 elementas \'kivi\':', sarasas)

# sarasas[1] = 'kakava' # 3
# print('\n3. uzd. 2 elementas pakeistas i \'kakava\':', sarasas)

# sarasas.remove('obuolys') # 4
# print('\n4. uzd. istrintas 1 elementas:', sarasas)

# del sarasas[2] # 5
# print('\n5. uzd. istrintas 3 elementas:', sarasas)

# print('\n6. uzd. elemento \'alus\' inexas:', sarasas.index('alus')) # 6

# sarasas.reverse() # 7
# print('\n7. uzd. sarasas atvirkstine tvarka:', sarasas)

# sarasas.pop(3) # 8
# print('\n8. uzd. is\'pop\'intas 4 elementas', sarasas)

# print('\ngalutinis sarasas: ', sarasas)


"""
# Penkta užduotis:
Patikrinkite sąrašo ilgį.
"""
# sarasas = ['obuolys', 'bananas', 'kriause', 'melionas', 'alus']
# print(len(sarasas))


"""
Šešta užduotis:
Patikrinkite ar tam tikras produktas yra sąraše.
"""
# sarasas = ['obuolys', 'bananas', 'kriause', 'melionas', 'alus']
# print('tikrinam ar yra obuolys:', 'obuolys' in sarasas)
# print('tikrinam ar yra vanduo:', 'vanduo' in sarasas)
