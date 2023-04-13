# Pirma užduotis:
def pirma_uzduotis():
    print("\nPirma užduotis: Parašykite programą, kuri leidžia vartotojui įvesti bet kokią simbolių eilutę ir atspausdina jos pirmąjį ir paskutinį simbolius")
    simboliu_eilute = str(input("Įveskite simbolių eilutę: "))
    print(simboliu_eilute[0],simboliu_eilute[-1])
# pirma_uzduotis()


# Antra užduotis:
def antra_uzduotis():
    print("\nAntra užduotis: Sukurkite simbolių eilutę, kurią sudaro jūsų mėgstamos knygos pavadinimas. Atspausdinkite jo pirmąsias penkias raides")
    simboliu_eilute = str(input("Įveskite mėgstamos knygos pavadinima: "))
    print(simboliu_eilute[:5])
# antra_uzduotis()


# Trecia užduotis:
def trecia_uzduotis():
    print("\nTrecia užduotis: Sukurkite simbolių eilutę, kurią sudaro jūsų mėgstama citata. Atspausdinkite jo paskutines tris raides")
    simboliu_eilute = str(input("Įveskite mėgstama citata: "))
    print(simboliu_eilute[-3:])
# trecia_uzduotis()


# Ketvirta užduotis:
def ketvirta_uzduotis():
    print("\nKetvirta užduotis: Sukurkite programą, kuri leidžia vartotojui įvesti du skirtingus žodžius ir atspausdina kiekvieno žodžio pirmuosius simbolius, atskirtus brūkšneliu")
    simboliu_eilute1 = (str(input("Įveskite pirma zodi: ")))
    simboliu_eilute2 = (str(input("Įveskite antra zodi: ")))
    print(simboliu_eilute1[0] + "-" + simboliu_eilute2[0])
# ketvirta_uzduotis()


# Penkta užduotis:
def penkta_uzduotis():
    print("\nPenkta užduotis: Sukurkite tekstą \"Aš esu studentas\"")
    simboliu_eilute = str(input("Įveskite teksta: "))
    print(simboliu_eilute.upper())
    print(simboliu_eilute.lower())
    print(simboliu_eilute.join())
    print(simboliu_eilute.split())
    print(simboliu_eilute.replace())
    
# penkta_uzduotis()

# Sesta užduotis:
def sesta_uzduotis():
    print("\nSesta užduotis: Paprašykite vartotojo įvesti savo vardą ir amžių. Tada išveskite pranešimą, kuriame nurodomi vartotojo vardas ir metai, kai vartotojui sukaks 100 metų.")
    vardas = str(input("Įveskite varda: "))
    amzius = str(input("Įveskite amziu: "))
    if amzius == '100':
        print("zdarowa seneliumbai, {}, tau jau: {},!".format(vardas, amzius))
# sesta_uzduotis()


# Septinta užduotis:
def septinta_uzduotis():
    print("\nSesta užduotis: Parašykite programą, kuri paprašytų vartotojo įvesti savo ūgį centimetrais. Tada programą turi paversti vartotojo ūgį metrais ir išvesti pranešimą su vartotojo ūgiu abiejomis matavimo vienetų.")
    ugis_cm = int(input("Įveskite savo ugi centimetrais: "))
    ugis_m = float(ugis_cm / 100)
    print("jusu ugis centimetrais, {}cm , jusu ugis metrais: {}m".format(ugis_cm, ugis_m))
# septinta_uzduotis()


# Astunta užduotis:
def astunta_uzduotis():
    print("\nAstunta užduotis: Paprašykite vartotojo įvesti savo atlyginimą ir taikomą mokesčio procentą. Tada apskaičiuokite, kiek vartotojas gaus mėnesio pabaigoje, kai nuo atlyginimo bus nuskaičiuotas mokesčio procentas.")
    atlyginimas = float(input("Įveskite savo atlyginimą: "))
    procentas = float(input("Įveskite savo taikomą mokesčio procentą tik skaiciais: "))
    procentas_skaiciavimui = float((100 - procentas) / 100)
    atlyginimas_i_rankas = float(atlyginimas * procentas_skaiciavimui)
    print("jusu atlyginimas i rankas yra, {:.2f} EUR".format(atlyginimas_i_rankas))
# astunta_uzduotis()


# Devinta užduotis:
def devinta_uzduotis():
    print("\nDevinta užduotis: Sukurkite programą, kuri leistų vartotojui pasirinkti, kokią konversiją jis nori atlikti: arba keisti temperatūrą iš laipsnių Celsijaus į laipsnius Farenheito, arba iš laipsnių Farenheito į laipsnius Celsijaus. Tada programa turi paprašyti vartotojo įvesti pradinę temperatūrą ir atlikti konversiją bei išvesti rezultatą.")
    sistema = str(input("Įveskite raide \"f\" jei norite konversijos F->C, Įveskite raide \"c\" jei norite konversijos C->F: "))
    laipsniai = float(input("Įveskite temperatūrą laipsniais: "))
    if sistema == 'c':
        fahrenheit = (laipsniai * 1.8) + 32
        print("{:.1f} laipsnių Celsijaus yra {:.1f} laipsnių Farenheitų.".format(laipsniai, fahrenheit))
    elif sistema == 'f':
        fahrenheit = (laipsniai - 32) * float(5/9)
        print("{:.1f} laipsnių Celsijaus yra {:.1f} laipsnių Farenheitų.".format(laipsniai, fahrenheit))
    else:
        print('kazkokia nesamone ivedei, krc bandyk  dar karta..')
# devinta_uzduotis()