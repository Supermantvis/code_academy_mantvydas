'''
Pirma užduotis
Sukurkite banko sąskaitos klasę, kuri turėtų kintamuosius: saskaitos numeris, savininkas, balansas ir pin kodas. Pastarieji du kintamieji turėtų būti privatūs.
Sukurkite metodą, kuris leistų nuskaityti pinigus nuo sąskaitos, tačiau norint atlikti šį veiksmą reikalingas slaptažodis, kuris turėtų būti žinomas tik klasės viduje.
Padarykite taip, kad būtų galima papildyti sąskaitą.
'''
# class BankoSaskaita:
#     def __init__(self, saskaitos_numeris, savininkas, balansas=75000, pin_kodas='1234'):
#         self.saskaitos_numeris = saskaitos_numeris
#         self.savininkas = savininkas
#         self.__balansas = balansas
#         self.__pin_kodas = pin_kodas

#     def nuskaityti_pinigus(self, pin, nuskaitoma_suma):
#         if pin == self.__pin_kodas:
#             self.__balansas = self.__balansas - nuskaitoma_suma
#             return self.__balansas
#         else:
#             print('NETEISINGAS PIN.')
#             return self.__balansas

#     def papildyti_saskaita(self, pin, pridedama_suma):
#         if pin == self.__pin_kodas:
#             self.__balansas = self.__balansas + pridedama_suma
#             return self.__balansas
#         else:
#             print('NETEISINGAS PIN.')
#             return self.__balansas

# banko_klientas = BankoSaskaita('LT06895045950660550', 'Jonas')

# # print(f"Tiek kachingo liko saskaitoje: {banko_klientas.nuskaityti_pinigus('1235', 5000)}")
# print(f"Tiek kachingo dabar yra saskaitoje: {banko_klientas.papildyti_saskaita('1234', 10000)}")


# SUGGESTED SOLUTION:
# class BankoSaskaita:
#     def __init__(self, saskaitos_numeris, savininkas, balansas, pin_kodas):
#         self.saskaitos_numeris = saskaitos_numeris
#         self.savininkas = savininkas
#         self.__balansas = balansas
#         self.__pin_kodas = pin_kodas

#     def nuskaityti(self, suma, pin_kodas):
#         if pin_kodas == self.__pin_kodas:
#             self.__balansas -= suma
#             print(f'{suma} € sėkmingai nuskaityta. Dabartinis saskaitos likutis: {self.__balansas} €')
#         else:
#             print('Neteisingas slaptažodis. Nuskaitymas negalimas.')

#     def papildyti(self, suma, pin_kodas):
#         if pin_kodas == self.__pin_kodas:
#             self.__balansas += suma
#             print(f'{suma} € sėkmingai papildyta. Dabartinis saskaitos likutis: {self.__balansas} €')
#         else:
#             print('Neteisingas slaptažodis. Papildymas negalimas.')

# saskaita = BankoSaskaita('LT123456789', 'Jonas Jonaitis', 1000, 1234)

# saskaita.nuskaityti(100, 1122)
# saskaita.nuskaityti(200, 1234)
# saskaita.nuskaityti(100, 1234)
# saskaita.papildyti(500, 1234)

'''
Antra užduotis
Sukurkite knygų klasę, kuri turėtų privačius kintamuosius: pavadinimas, autorius, buklė ir puslapių skaičius, ir metodus jiems gauti.
Sukurkite metodą, kuris leistų pakeisti knygos būklę, kur galimos reikšmės yra tik 'patenkinama', 'prasta', 'atnaujinta', 'sugadinta'.
Sukurkite metodą, kuris leistų sumažinti knygos puslapių skaičių, naudodamas sukurtą vidinį privatų metodą, perrašantį tą reikšmę. Turi neigi padidinti puslapių skaičiaus.
'''
# class Knygos:
#     def __init__(self, pavadinimas='The Lord of the Rings', autorius='J. R. R. Tolkien', bukle='nauja', puslapiu_skaicius=1178):
#         self.__pavadinimas = pavadinimas
#         self.__autorius = autorius
#         self.__bukle = bukle
#         self.__puslapių_skaicius = puslapiu_skaicius

#     def gauti_pavadinimas(self):
#         return self.__pavadinimas

#     def gauti_autorius(self):
#         return self.__autorius

#     def gauti_bukle(self):
#         return self.__bukle

#     def gauti_puslapių_skaicius(self):
#         return self.__puslapių_skaicius

#     def keisti_knygos_bukle(self, bukle):
#         print('atnaujinkite knygos bukle (galimi variantai: \'patenkinama\', \'prasta\', \'atnaujinta\', \'sugadinta\')')
#         if bukle == 'patenkinama':
#             self.__bukle = bukle
#         elif bukle == 'prasta':
#             self.__bukle = bukle
#         elif bukle == 'atnaujinta':
#             self.__bukle = bukle
#         elif bukle == 'sugadinta':
#             self.__bukle = bukle
#         else:
#             print('Ivesta netinkama bukle.')
#         return self.__bukle  # USE return TO BE ABLE PRINT IMMEDIATELY

#     def __keisti_puslapiu_skaiciu(self, naujas_puslapiu_skaicius):
#         self.__puslapių_skaicius = self.__puslapių_skaicius - naujas_puslapiu_skaicius

#     def sumazinti_puslapiu_skaiciu(self, naujas_puslapiu_skaicius):
#         self.__keisti_puslapiu_skaiciu(naujas_puslapiu_skaicius)


# knyga = Knygos()

# print(knyga.gauti_pavadinimas())
# print(knyga.gauti_autorius())
# print(knyga.gauti_bukle())
# print(knyga.gauti_puslapių_skaicius())
# # print(knyga.keisti_knygos_bukle('belekas'))
# print(knyga.keisti_knygos_bukle('sugadinta'))

# knyga.sumazinti_puslapiu_skaiciu(50)
# print(knyga.gauti_puslapių_skaicius())


# SUGGESTED SOLUTION:
# class Knyga:
#     def __init__(self, pavadinimas, autorius, bukle, puslapiai):
#         self.__pavadinimas = pavadinimas
#         self.__autorius = autorius
#         self.__bukle = bukle
#         self.__puslapiai = puslapiai

#     def gauti_pavadinima(self):
#         return self.__pavadinimas

#     def gauti_autoriu(self):
#         return self.__autorius

#     def gauti_bukle(self):
#         return self.__bukle

#     def gauti_puslapius(self):
#         return self.__puslapiai

#     def pakeisti_bukle(self, bukle):
#         if bukle in ('patenkinama', 'prasta', 'atnaujinta', 'sugadinta'):
#             self.__bukle = bukle
#         else:
#             print(f'negalima pakeisti būklės į {bukle}.')

#     def __naujas_puslapiu_skaicius(self, puslapiai):
#         self.__puslapiai = puslapiai

#     def isplesti_puslapius(self, puslapiai):
#         if abs(puslapiai) <= self.__puslapiai:
#             self.__naujas_puslapiu_skaicius(self.__puslapiai - abs(puslapiai))
#         else:
#             self.__puslapiai = 0

# knyga = Knyga("Python programavimo kalba", "Guido van Rossum", 'nauja', 400)

# knyga.isplesti_puslapius(50)
# knyga.pakeisti_bukle('prasta')
# print(knyga.gauti_pavadinima())
# print(knyga.gauti_autoriu())
# print(knyga.gauti_bukle())
# print(knyga.gauti_puslapius())


'''
Trecia uzduotis: automobilio rida, turi eiti skaičiuoti kilometrus automobilio ridai tik į priekį.
'''
# class Automobilis:
#     def __init__(self, marke, modelis, rida=80000):
#         self.marke = marke
#         self.modelis = modelis
#         self.__rida = rida

#     def dabartine_rida(self):
#         return self.__rida

#     def __nauja_rida(self, ridos_rodmenys):  # NEVEIKIA!!!
#         self.__rida = ridos_rodmenys

#     def didinti_rida(self, ridos_rodmenys):  # NEVEIKIA!!!
#         if abs(ridos_rodmenys) < 0:
#             self.__nauja_rida(self.__rida + abs(ridos_rodmenys))
#         else:
#             self.__rida = 0


# masina = Automobilis("Testa", "Model S")

# masina.didinti_rida(5000)
# print(masina.dabartine_rida())


class Automobilis:  # PAPRASTAS PVZ
    def __init__(self, marke, modelis, metai=2023, spalva='pilka'):
        self.marke = marke
        self.modelis = modelis
        self.__metai = metai
        self.__spalva = spalva

    def gauti_metus(self):
        return self.__metai

    def gauti_spalva(self):
        return self.__spalva

    def __keisti_spalva(self, nauja_spalva):
        self.__spalva = nauja_spalva

    def perdazyti(self, nauja_spalva):
        self.__keisti_spalva(nauja_spalva)


trecias_automobilis = Automobilis('Mercedes', 'C-Class')
trecias_automobilis.perdazyti('raudona')
print(trecias_automobilis.gauti_spalva()) # raudona
