'''
Pirma užduotis
Sukurkite funkciją apskritimo_plotas, kuri priima 2 argumentus: apskritimo spindulys ir pi reikšmę. Jei funkcija kviečiama be pi argumento, jis turėtų būti nustatytas į numatytąją reikšmę 3.14. Funkcija turi grąžinti apskritimo plotą.
'''

# def apskritimo_plotas(apskritimo_spindulys, pi_reiksme=3.14):
#     apskritimo_plotas = pi_reiksme*(apskritimo_spindulys**2)
#     return apskritimo_plotas

# print(apskritimo_plotas(30))


# def apskritimo_plotas(spindulys, pi=3.14):  # SUGGESTED SOLUTION
#     plotas = pi * (spindulys ** 2)
#     return plotas


'''
Antra užduotis
Parašykite funkciją keliones_informacija, kuri turi šiuos argumentus:

keliones_trukme: privalomas argumentas, nurodantis kelionės trukmę valandomis.
greitis: privalomas argumentas, nurodantis vidutinį greitį km/h.
vartojimas: neprivalomas argumentas, nurodantis vidutinį kuro sąnaudų kiekį su numatyta reikšme 7 (l/100 km.)
kuro_kaina: neprivalomas argumentas su numatyta reikšme 1.2 (kuro kaina eurais už litrą).
Funkcija turėtų grąžinti šią informaciją:

Nuvažiuotas atstumas (atstumas = keliones_trukme * greitis).
Bendros kelionės kuro sąnaudos (sąnaudos = atstumas * vartojimas / 100).
Bendros kelionės išlaidos kuras (išlaidos = sąnaudos * kuro_kaina).
Funkcija turi grąžinti šią informaciją kaip žodyną.
'''

# keliones_informacija_dict = {}

# def keliones_informacija(keliones_trukme, greitis, vartojimas=7, kuro_kaina=1.2):
#     atstumas = keliones_trukme * greitis
#     sanaudos = atstumas * vartojimas / 100
#     islaidos = sanaudos * kuro_kaina
#     keliones_informacija_dict['atstumas'] = atstumas
#     keliones_informacija_dict['sanaudos'] = sanaudos
#     keliones_informacija_dict['islaidos'] = islaidos

#     return keliones_informacija_dict

# print(keliones_informacija(2, 100))


# def keliones_informacija(keliones_trukme, greitis, vartojimas=7, kuro_kaina=1.2):  # SUGGESTED SOLUTION
#     atstumas = keliones_trukme * greitis
#     sąnaudos = atstumas * vartojimas / 100
#     išlaidos = sąnaudos * kuro_kaina
    
#     return {
#         'atstumas': atstumas,
#         'sąnaudos': sąnaudos,
#         'išlaidos': išlaidos
#     }
