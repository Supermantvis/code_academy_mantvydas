'''
Pirma užduotis
Sukurkite banko sąskaitos klasę, kuri turėtų kintamuosius: saskaitos numeris, savininkas, balansas ir pin kodas. Pastarieji du kintamieji turėtų būti privatūs.
Sukurkite metodą, kuris leistų nuskaityti pinigus nuo sąskaitos, tačiau norint atlikti šį veiksmą reikalingas slaptažodis, kuris turėtų būti žinomas tik klasės viduje.
Padarykite taip, kad būtų galima papildyti sąskaitą.
'''
class BankoSaskaita():
    def __init__(self, sask_numeris, savininkas, balansas=50000, pin_kodas=1234):
        self.sask_numeris = sask_numeris
        self.savininkas = savininkas
        self.__balansas = balansas
        self.__pin_kodas = pin_kodas

    def pinigu_nuskaitymas(self, nuskaitomas_kiekis, pin):
        if self.__balansas - nuskaitomas_kiekis >= 0 and pin == 1234:
            return self.__balansas - nuskaitomas_kiekis
        else:
            print('Bandote nuskaityti daugiau pinigu, negu yra saskaitoje arba ivedete neteisinga pin koda')

transakcija = BankoSaskaita('Petras', 'Petraitis')
print(transakcija.pinigu_nuskaitymas(5000, 1235))

'''
Antra užduotis
Sukurkite knygų klasę, kuri turėtų privačius kintamuosius: pavadinimas, autorius, buklė ir puslapių skaičius, ir metodus jiems gauti.
Sukurkite metodą, kuris leistų pakeisti knygos būklę, kur galimos reikšmės yra tik 'patenkinama', 'prasta', 'atnaujinta', 'sugadinta'.
Sukurkite metodą, kuris leistų sumažinti knygos puslapių skaičių, naudodamas sukurtą vidinį privatų metodą, perrašantį tą reikšmę. Turi neigi padidinti puslapių skaičiaus.
'''




'''
Trecia uzduotis: automobilio rida, turi eiti skaičiuoti kilometrus automobilio ridai tik į priekį.
'''

