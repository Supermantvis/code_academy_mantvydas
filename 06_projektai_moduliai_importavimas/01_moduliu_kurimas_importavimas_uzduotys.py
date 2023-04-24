'''
Pirma užduotis
Sukurkite naują Python modulį, pavadinimu matematika.py, kuriame būtų šios funkcijos:

daugyba(x, y): grąžina dviejų skaičių x ir y sandaugą
dalyba(x, y): grąžina dviejų skaičių x ir y dalmenį
Tada importuokite šį modulį kitame Python faile ir panaudokite jo funkcijas skaičiavimams atlikti.
'''
# from matematika import daugyba
# from matematika import dalyba

# print(daugyba(2, 5))
# print(dalyba(56, 80))


'''
Antra užduotis
Sukurkite paketą geometrija, kuris turėtų šiuos modulius:

apskritimas.py: turintis funkciją apskritimo_plotas(r) skirtą apskaičiuoti apskritimo plotą
kvadratas.py: turintis funkciją kvadrato_plotas(a) skirtą apskaičiuoti kvadrato plotą
Importuokite šiuos modulius kitame faile, pakeiskite funkcijų pavadinimus pasitelkiant as ir panaudokite funkcijas skaičiavimams atlikti.
'''

from geometrija.apskritimas import apskritimo_plotas as circle_area
from geometrija.kvadratas import kvadrato_plotas as square_area

print(circle_area(5))
print(square_area(5))