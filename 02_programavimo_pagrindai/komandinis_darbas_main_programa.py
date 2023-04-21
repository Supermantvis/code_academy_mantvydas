import random


# def zaidimukas_atspek_skaiciu(): # zaidimas atspeti skaiciu nuo 1 iki 10
#     print("\nAtspek skaiciu nuo 1 iki 10")
#     mano_skaicius = int(input("Iveskite savo skaiciu: "))
#     ai_skaicius = random.randint(1, 10)
#     if mano_skaicius == ai_skaicius:
#         print(("oho atspejai! >:0, mano skaicius buvo: ").upper(), ai_skaicius)
#     elif mano_skaicius != ai_skaicius:
#         print("neatspejai, bandyk dar karta ;) mano skaicius buvo: ", ai_skaicius)
#     else:
#         print("kazkokia nesamone ivedei, krc bandyk  dar karta..\n")


def komandu_paskirstytojas(): # programele sugeneruoti komandas atsitikine tvarka
    zmogeliukai = [
]

"""
TEAM LEADS:

"""

    zmoniu_suma_sarase = len(zmogeliukai)
    komandu_kiekis = 3

    while zmoniu_suma_sarase > 0:
        komanda = random.sample(zmogeliukai, int(zmoniu_suma_sarase/komandu_kiekis))
        for zmogus in komanda:
            zmogeliukai.remove(zmogus)
        zmoniu_suma_sarase -= int(zmoniu_suma_sarase/komandu_kiekis)
        komandu_kiekis -= 1
        print("\nKomanda Nr.", (3-komandu_kiekis), komanda)


# zaidimukas_atspek_skaiciu()
komandu_paskirstytojas()