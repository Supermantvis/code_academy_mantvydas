'''
Užduotys
TDD principu parašykite programą "paskolos kalkuliatorius".

sukurkite testą paskolos kalkuliatoriaus programai, kur paskolos objektui galima nustatyti paskolos dydį, metines palūkanas ir terminą.+

Testavimo scenarijus turi patikrinti kelis teisingus paskolos palūkanų, pabrangimo, mokėjimo grafiko scenarijus.

sukurkite programą, kuri veikia su aukščiau įgyvendintu testu.
'''
class PaskolosKalkuliatorius:
    #  Amortizing loan (formula) = amount of principal and interest paid each month over the course of your loan term
    #  P = a   /   { [ (1 + r) ^ n ] - 1 }   /   [ r * (1 + r) ^ n]
    
    #  P is your monthly loan payment
    #  a is your principal
    #  r is your periodic interest rate, which is your interest rate divided by 12
    #  n is the total number of months in your loan term

    #  monthly payment = principal x (interest rate / 12)

    #  palukanu_norma yra israiska procentais: 5% -> ivesti 0.05
    #  terminas yra israiska metais: 12men -> ivesti 1 | 6men -> ivesti 0.5
    def __init__(self, paskolos_suma, palukanu_norma, terminas, mokejimu_periodas=12):
        self.paskolos_suma = paskolos_suma
        self.palukanu_norma = palukanu_norma
        self.terminas = terminas
        self.mokejimu_periodas = mokejimu_periodas

    def periodine_imoka(self):
        #  P = a ÷ (X ÷ Y)
        a = self.paskolos_suma
        r = self.palukanu_norma / self.mokejimu_periodas
        n = self.mokejimu_periodas * self.terminas
        X = ((1 + r) ** n) - 1
        Y = r * (1 + r) ** n
        P = a / (X / Y)
        return P
    
    def paskolos_palukanu_suma(self):
        n = self.mokejimu_periodas * self.terminas
        palukanu_suma = (self.periodine_imoka() * n) - self.paskolos_suma
        return palukanu_suma

    # def tik_principal(self):  # TESTAS
    # #  P = a (r / n)
    # #  P is your monthly loan payment
    # #  a is your principal
    # #  r is your interest rate
    # #  n is the number of payments you make each year (which is 12)
    #     a = self.paskolos_suma
    #     r = self.palukanu_norma
    #     n = self.mokejimu_periodas
    #     P = a * (r / n)
    #     return P

if __name__ == "__main__":
    skolininkas = PaskolosKalkuliatorius(10000, 0.05, 5)
    print(f"Periodine paskolos imoka: {skolininkas.periodine_imoka():.2f} EUR")
    print(f"Viso termino grazintina palukanu suma: {skolininkas.paskolos_palukanu_suma():.2f} EUR")
    # print(f"TESTAS: {skolininkas.tik_principal():.2f} EUR")

