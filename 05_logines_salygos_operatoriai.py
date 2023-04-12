# Pirma užduotis:
def pirma_uzduotis():
    print("\nPirma užduotis: Parašykite programą, kuri nustatytų, ar vartotojo įvestas skaičius yra teigiamas, naudodami \"daugiau\" operatorių.")
    skaicius = int(input("Įveskite savo Skaičiu: "))
    if skaicius > 0:
        print("Skaičius yra teigiamas")
    else:
        print("Skaičius yra neigiamas")


# Antra užduotis:
def antra_uzduotis():
    print("\nAntra užduotis: Parašykite programą, kuri patikrintų, ar vartotojo įvestas skaičius yra tarp 5 ir 10, naudodama mažiau arba lygu operatorių.")
    skaicius = int(input("Įveskite savo Skaičiu: "))
    if skaicius >= 5 and skaicius <= 10:
        print("Skaičius yra tarp 5 ir 10")
    else:
        print("Skaičius nėra tarp 5 ir 10")


# Trečia užduotis:
def trecia_uzduotis():
    print("\nTrecia užduotis: Parašykite programą, kuri patikrintų, ar du skaičiai yra didesni nei 0, naudodami \"ir\" operatorių.")
    skaicius1 = int(input("Įveskite pirma Skaičiu: "))
    skaicius2 = int(input("Įveskite antra Skaičiu: "))
    if skaicius1 > 0 and skaicius2 > 0:
        print("Abu skaičiai yra didesni nei 0")
    else:
        print("Bent vienas skaičius yra neigiamas arba lygus 0")


# Ketvirta užduotis:
def ketvirta_uzduotis():
    print("\nKetvirta užduotis: Parašykite programą, kuri nustatytų, ar bent vienas duotų skaičių yra lyginis, naudodami \"arba\" operatorių.")
    skaicius1 = int(input("Įveskite pirma Skaičiu: "))
    skaicius2 = int(input("Įveskite antra Skaičiu: "))

    if (skaicius1 % 2) == 0 or (skaicius2 % 2) == 0:
        print("Bent vienas skaičius yra lyginis")
    else:
        print("Abu skaičiai yra nelyginiai")


pirma_uzduotis()
antra_uzduotis()
trecia_uzduotis()
ketvirta_uzduotis()