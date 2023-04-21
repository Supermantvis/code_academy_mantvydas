'''
Pirma užduotis
Sukurti naują klasę Darbuotojas, turinčią savybes vardas, pavardė, pareigos ir atlyginimas (su numatyta minimalia alga)
Sukurti naują objektą darbuotojas
Atspausdinkite darbuotojo pareigas ir atlyginimą.
Pakeisti darbuotojo atlyginimą.
Atspausdinkite pilną darbuotojo informaciją.
'''
# class Darbuotojas:
#     vardas = 'Jonas'
#     pavardė = 'Jonaitis'
#     pareigos = 'Programuotojas'
#     atlyginimas = '900'

# darbuotojas = Darbuotojas()

# print(darbuotojas.pareigos)
# print(darbuotojas.atlyginimas)

# darb1 = darbuotojas.atlyginimas = 1500

# print('pakeistas atlyginimas: ', darbuotojas.atlyginimas)

# # for key, value in darbuotojas.items():  # NEVEIKIA...
# #     print(key, value)


# SUGGESTED SOLUTION:
# class Darbuotojas:
#     def __init__(self, vardas, pavarde, pareigos, atlyginimas=1000):
#         self.vardas = vardas
#         self.pavarde = pavarde
#         self.pareigos = pareigos
#         self.atlyginimas = atlyginimas

    # def __str__(self):
    #     return f'{self.vardas} {self.pavarde}, pareigos: {self.pareigos}, atlyginimas: {self.atlyginimas}'

# darbuotojas = Darbuotojas('Jonas', 'Jonaitis', 'Programuotojas', 2000)

# print('Darbuotojo pareigos:', darbuotojas.pareigos)
# print('Darbuotojo atlyginimas:', darbuotojas.atlyginimas)

# darbuotojas.atlyginimas = 2500

# print('Darbuotojas:', darbuotojas)

'''
Antra užduotis
Sukurkite klasę "Gyvūnas" su savybėmis: vardas, amžius ir svoris.
Sukurkite __str__ metodą patogiam informacijos apie gyvūną grąžinimui
Sukurkite metodus padidinti ir sumažinti svorį.
Sukurkite metodą gimtadienis, padidinantį amžių.
Sukurkite objektą su jūsų pasirinktomis reikšmėmis.
Atspausdinkite objektą.
Pakeiskite kelis kartus gyvūno svorį ir amžių naudojant sukurtus metodus ir po kiekvieno pakeitimo atspausdinkite.
'''

# class Gyvunas:
#     def __init__(self, vardas, amzius, svoris):
#         self.vardas = vardas
#         self.amzius = amzius
#         self.svoris = svoris

#     def __str__(self):
#         return f'Vardas: {gyvunas.vardas}, Amzius: {gyvunas.amzius}, Svoris: {gyvunas.svoris}'

#     def dididnti_svori(self, kiekis):  # isoreje galima iskarto kviesti taip: print(gyvunas.dididnti_svori(2))
#         self.svoris += kiekis  # KO GERO SITAS VARIANTAS YRA GERESNIS...
#         return self.svoris
    
#     # def dididnti_svori(self, kiekis):  # isoreje pirma reikia ivykdyti operacija: gyvunas.dididnti_svori(2)
#     #     self.svoris += kiekis  # ir tik paskiau atvaizduoti: print(gyvunas.svoris)
    
#     # def mazinti_svori(self, kiekis):  # isoreje galima iskarto kviesti taip: print(gyvunas.mazinti_svori(2))
#     #     self.svoris -= kiekis
#     #     return self.svoris
    
#     def mazinti_svori(self, kiekis):  # isoreje pirma reikia ivykdyti operacija: gyvunas.mazinti_svori(2)
#         self.svoris -= kiekis  # ir tik paskiau atvaizduoti: print(gyvunas.svoris)

#     def gimtadienis(self, kiekis):
#         self.amzius += kiekis
#         return self.amzius


# gyvunas = Gyvunas('Toto', 13, 120)  # objekto sukurimas
# print(f'Pirmas objekto aprasymas{gyvunas}')
# print(f'Didinam svori: {gyvunas.dididnti_svori(2)}')
# gyvunas.mazinti_svori(2)
# print(f'Mazinam svori: {gyvunas.svoris}')
# print(f'Svenciam gimtadieni: {gyvunas.gimtadienis(10)}')


# gyvunas = Gyvunas('ALFA', 5, 10)
# print(f'Antras objekto aprasymas{gyvunas}')
# print(f'Didinam svori: {gyvunas.dididnti_svori(2)}')
# gyvunas.mazinti_svori(2)
# print(f'Mazinam svori: {gyvunas.svoris}')
# print(f'Svenciam gimtadieni: {gyvunas.gimtadienis(10)}')


# SUGGESTED SOLUTION:
# class Gyvunas:
#     def __init__(self, vardas, amzius, svoris):
#         self.vardas = vardas
#         self.amzius = amzius
#         self.svoris = svoris
    
#     def padidinti_svori(self, kiek):
#         self.svoris += kiek
    
#     def sumazinti_svori(self, kiek):
#         self.svoris -= kiek

#     def gimtadienis(self):
#         self.amzius += 1
        
#     def __str__(self):
#         return f'Gyvūnas vardu {self.vardas} yra {self.amzius} metų ir sveria {self.svoris} kg'

# gyvunas = Gyvunas('Reksas', 5, 20)
# print(gyvunas)

# gyvunas.padidinti_svori(5)
# print(gyvunas)

# gyvunas.gimtadienis()
# print(gyvunas)

# gyvunas.sumazinti_svori(3)
# print(gyvunas)