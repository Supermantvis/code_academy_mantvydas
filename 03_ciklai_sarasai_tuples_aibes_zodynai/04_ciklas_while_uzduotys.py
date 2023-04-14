"""
Pirma užduotis
Turite skaičių lygų 10. Atspausdinkite skaičiaus mažinimo ciklą, kol jis pasieks -1.
"""
# skaicius = 10
# while skaicius > -1:
#     print(skaicius)
#     skaicius -= 1
# else:
#     print('skaicius patapo 1, ciklo pabaiga.')


# skaicius = 10  # SUGGESTED SOLUTION
# while skaicius >= -1:
#     print(skaicius)
#     skaicius -= 1

"""
Antra užduotis
Turite skaičių lygų 5. Atspausdinkite skaičiaus mažinimo ciklą, kol jis pasieks -10, tačiau sustabdykite ciklą, kai skaičius bus lygus -5, bet pratęskite, jeigu skaičius bus lygus 0.
"""
# skaicius = 5
# while skaicius >= -10:
#     print(skaicius)
#     skaicius -= 1
#     if skaicius == 0:
#         print('skaicius patapo 0, skippinam zingsni.')
#         continue
#     elif skaicius == -5:
#         print('skaicius patapo -5, ciklo pabaiga.')
#         break


# skaicius = 5  # SUGGESTED SOLUTION
# while skaicius >= -10:
#     skaicius -= 1
#     if skaicius == -5:
#         print('Sustabdomas ciklas, nes pasiektas skaičius -5')
#         break
#     elif skaicius == 0:
#         print('Pratęsiame ciklą, nes pasiektas skaičius 0')
#         continue
#     print(skaicius)


"""
Trečia užduotis
Parašyti programą, kuri:

Leistų vartotojui įvesti skaičių.
Jei įvestas skaičius yra teigiamas, paprašyti įvesti dar vieną skaičių
Jei įvestas skaičius neigiamas, nutraukti programą ir atspausdinti visų įvestų teigiamų skaičių sumą
Patarimas: Naudoti ciklą while, sąlygą if, break
"""

# skaiciu_list = []
# while True:
#     ivestas_skaicius = int(input('iveskite skaiciu: '))
#     if (0 + ivestas_skaicius) >= 0:
#         skaiciu_list.append(ivestas_skaicius)
#     if (0 + ivestas_skaicius) < 0:
#         print(sum(skaiciu_list))
#         break


# suma = 0  # SUGGESTED SOLUTION

# while True:
#     skaicius = int(input('Įveskite skaičių: '))
#     if skaicius < 0:
#         break
#     suma += skaicius

# print(suma)
