'''
Pirma užduotis
Parašykite programą, kuri leistų vartotojui įvesti teigiamą skaičių.
Programa turi sugauti galimas klaidas.
'''
def skaiciaus_tikrinimas(skaicius):
    if skaicius == 0:
        raise ValueError("Jusu skaicius yra nulis")
    elif skaicius < 0:
        raise ValueError("Jusu skaicius yra neigimas")
    elif type(skaicius) != int:
        raise ValueError("Jusu skaicius yra ne skaicius")
    else:
        print("Jusu ivestas skaicius yra teigiamas")
        return skaicius
    
skaiciaus_tikrinimas('h')


# SUGGESTED SOLUTION:
# while True:
#     try:
#         skaicius = float(input("Įveskite teigiamą skaičių: "))
#         if skaicius <= 0:
#             raise ValueError("Įvestas skaičius yra neigiamas")
#         else:
#             print("Ačiū, jūs įvedėte:", skaicius)
#             break
#     except ValueError as error:
#         print("Klaida:", error)