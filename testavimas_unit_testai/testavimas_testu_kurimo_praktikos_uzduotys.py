'''
Užduotys
TDD principu parašykite programą "paskolos kalkuliatorius".

sukurkite testą paskolos kalkuliatoriaus programai, kur paskolos objektui galima nustatyti paskolos dydį, metines palūkanas ir terminą.+

Testavimo scenarijus turi patikrinti kelis teisingus paskolos palūkanų, pabrangimo, mokėjimo grafiko scenarijus.

sukurkite programą, kuri veikia su aukščiau įgyvendintu testu.
'''
class PaskolosKalkuliatorius:
    #  palukanu_norma yra procentais: 5% -> palukanu_norma = 0.05
    #  terminas yra metais: 12men -> terminas == 1 | 12men -> terminas ==  0.5.
    def __init__(self, paskolos_dydis, palukanu_norma, terminas):
        self.paskolos_dydis = paskolos_dydis
        self.palukanu_norma = palukanu_norma
        self.terminas = terminas

    def menesine_imoka(self):
        grazintina_suma = self.paskolos_dydis * (1 + (self.palukanu_norma / 100))
        laikotarpis_menesiais = self.terminas * 12
        menesine_imoka = grazintina_suma / laikotarpis_menesiais
        return menesine_imoka
    
    def pabrangimo_suma(self):
        grazintina_suma = self.paskolos_dydis * (1 + (self.palukanu_norma / 100))
        return grazintina_suma - self.paskolos_dydis


if __name__ == "__main__":
    skolininkas = PaskolosKalkuliatorius(10000, 5, 5)
    print(skolininkas.menesine_imoka())
    # print(skolininkas.pabrangimo_suma())