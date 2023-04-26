'''
Pirma užduotis
Sukurkite banko sąskaitos klasę, kuri turėtų kintamuosius: saskaitos numeris, savininkas, balansas ir pin kodas. Pastarieji du kintamieji turėtų būti privatūs.
Sukurkite metodą, kuris leistų nuskaityti pinigus nuo sąskaitos, tačiau norint atlikti šį veiksmą reikalingas slaptažodis, kuris turėtų būti žinomas tik klasės viduje.
Padarykite taip, kad būtų galima papildyti sąskaitą.
'''
# class BankoSaskaita():
#     def __init__(self, sask_numeris, savininkas, balansas=50000, pin_kodas=1234):
#         self.sask_numeris = sask_numeris
#         self.savininkas = savininkas
#         self.__balansas = balansas
#         self.__pin_kodas = pin_kodas

#     # def __str__(self):
#     #     return f'Saskaitos numers:{self.sask_numeris}, savininkas:{self.savininkas}, balansas{self.__balansas}'

#     def pinigu_nuskaitymas(self, nuskaitomas_kiekis, pin):
#         if self.__balansas - nuskaitomas_kiekis >= 0 and pin == self.__pin_kodas:
#             return self.__balansas - nuskaitomas_kiekis
#         else:
#             print('Bandote nuskaityti daugiau pinigu, negu yra saskaitoje arba ivedete neteisinga pin koda')

#     def saskaitos_papildymas(self, pridedamas_kiekis, pin):
#         if pin == self.__pin_kodas:
#             return self.__balansas + pridedamas_kiekis
#         else:
#             print('Ivedete neteisinga pin koda')

# transakcija = BankoSaskaita('LT056265056620', 'Petras Petraitis')
# # print(transakcija.pinigu_nuskaitymas(5000, 1234))
# print(transakcija.saskaitos_papildymas(15000, 1234))


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
class Knygos():
    def __init__(self, pavadinimas="The Lord of the Rings", autorius="J. R. R. Tolkien", bukle="Nauja", puslapiu_skaicius=1178):
        self.pavadinimas = pavadinimas
        self.autorius = autorius
        self.bukle = bukle
        self.puslapiu_skaicius = puslapiu_skaicius

    def knygos_pavadinimas(self):
        return self.pavadinimas

    def knygos_autorius(self):
        return self.autorius

    def knygos_bukle(self):
        return self.bukle

    def knygos_puslapiu_skaicius(self):
        return self.puslapiu_skaicius



knyga = Knygos()
print(knyga.knygos_pavadinimas())
print(knyga.knygos_autorius())
print(knyga.knygos_bukle())
print(knyga.knygos_puslapiu_skaicius())


'''
Trecia uzduotis: automobilio rida, turi eiti skaičiuoti kilometrus automobilio ridai tik į priekį.
'''

