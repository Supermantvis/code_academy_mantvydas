'''
Pirma užduotis
Sukurti naują klasę Darbuotojas, turinčią savybes vardas, pavardė, pareigos ir atlyginimas (su numatyta minimalia alga)
Sukurti naują objektą darbuotojas
Atspausdinkite darbuotojo pareigas ir atlyginimą.
Pakeisti darbuotojo atlyginimą.
Atspausdinkite pilną darbuotojo informaciją.
'''
# class Darbuotojas:
#     def __init__(self, vardas, pavarde, pareigos, atlyginimas=1000):
#         self.vardas = vardas
#         self.pavarde = pavarde
#         self.pareigos = pareigos
#         self.atlyginimas = atlyginimas

#     def __str__(self):
#         return f'{self.vardas} {self.pavarde} {self.pareigos} {self.atlyginimas}'

# darbuotojas = Darbuotojas('Jonas', 'Jonaitis', 'suvirintojas')

# print(darbuotojas.pareigos)
# print(darbuotojas.atlyginimas)

# darbuotojas.atlyginimas = 1200
# print(darbuotojas.atlyginimas)

# print(darbuotojas)


# ******************* SUGGESTED SOLUTION: *******************
# class Darbuotojas:
#     def __init__(self, vardas, pavarde, pareigos, atlyginimas=1000):
#         self.vardas = vardas
#         self.pavarde = pavarde
#         self.pareigos = pareigos
#         self.atlyginimas = atlyginimas

#     def __str__(self):
#         return f'{self.vardas} {self.pavarde}, pareigos: {self.pareigos}, atlyginimas: {self.atlyginimas}'

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
#     def __init__(self, vardas='Bungis', amzius=25, svoris=60):
#         self.vardas = vardas
#         self.amzius = amzius
#         self.svoris = svoris

#     def __str__(self):
#         return f'Vardas: {self.vardas} | Amzius: {self.amzius} | Svoris: {self.svoris}'

#     def sumazinti_svori(self, pokytis):
#         return self.svoris - pokytis

#     def padidinti_svori(self, pokytis):
#         return self.svoris + pokytis

# gyvunas = Gyvunas()
# print(gyvunas)

# gyvunas.svoris = gyvunas.sumazinti_svori(2)
# print(gyvunas)

# gyvunas.svoris = gyvunas.padidinti_svori(4)
# print(gyvunas)

# gyvunas = Gyvunas('Toto', 7, 20)
# print(gyvunas)


# ******************* SUGGESTED SOLUTION: *******************
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