'''
Pirma užduotis
Atidarykite tekstiniame faile esančią eilutę ir atspausdinkite ją, pakeičiant visus didžiąsias raides mažosiomis ir atvirkščiai. Failo pavadinimas: "pakeitimai.txt".💡 Galite naudoti swapcase() funkciją.
'''
# with open('08_darbas_su_failais/mano_failas.txt', 'r') as failas:
#     for eilute in failas:
#         if eilute == eilute.upper():
#             print(eilute.lower())
#         else:
#             print(eilute.upper())


# SUGGESTED SOLUTION:
# with open("08_darbas_su_failais/mano_failas.txt", "r") as failas:
#     eilute = failas.readline()
#     nauja_eilute = eilute.swapcase()
#     print(nauja_eilute)


'''
Antra užduotis
Sukurkite naują failą "skaiciai.txt" ir įrašykite į jį skaičius nuo 1 iki 100, kiekvieną naujoje eilutėje.
'''
# with open('08_darbas_su_failais/skaiciai.txt', 'w+') as failas:
#     i = 0
#     for eilute in range(100):
#         i =+ 1
#         failas.write(str(i))
#         failas.write('\n')

# # SUGGESTED SOLUTION:
# with open("skaiciai.txt", "w") as failas:
#     for skaicius in range(1, 101):
#         failas.write(f"{skaicius}\n")


'''
Trečia užduotis
Atidarykite "tekstas.txt" failą, pakeiskite failo žymeklį į vidurį failo ir atspausdinkite likusį failo turinį.
'''
# with open('08_darbas_su_failais/mano_failas.txt', 'r') as failas:
#     char_sum = 0
#     for eilute in failas:
#         for char in eilute:
#             char_sum += 1
#     file_middle = char_sum / 2
#     failas.seek(file_middle)
#     antra_failo_dalis = failas.read()
# print(antra_failo_dalis, 2)


# SUGGESTED SOLUTION:
# with open("tekstas.txt", "r") as failas:
#     failas.seek(0, 2)  # Pereikite į failo pabaigą
#     failo_ilgis = failas.tell()  # Gauti failo ilgį
#     vidurys = failo_ilgis // 2  # Rasti failo vidurį

#     failas.seek(vidurys)  # Nustatykite žymeklį ant vidurio
#     likusi_dalis = failas.read()  # Perskaitykite likusią dalį
#     print(likusi_dalis)


'''
Ketvirta užduotis
Sukurkite failą "eilutes.txt" ir įrašykite į jį šias eilutes:
Saulėlydis žėri žemę švelniai.
Vakare vėjas šnypščia medžius.
Vėjas nerimsta, šnypščia ir švilpia.

Papildykite failą "eilutes.txt" nauja eilute, kuri yra jūsų vardas ir pavardė.

Atidarykite "eilutes.txt" failą, perskaitykite jo turinį ir atspausdinkite visas eilutes, kuriose yra žodis "vėjas"
'''
# eilutes = [
#     "Saulėlydis žėri žemę švelniai.\n",
#     "Vakare vėjas šnypščia medžius.\n",
#     "Vėjas nerimsta, šnypščia ir švilpia.\n"
#     ]

# with open('08_darbas_su_failais/eilutes.txt', 'w+', encoding='utf-8') as failas:
#     failas.writelines(eilutes)
#     failas.write("Mantvydas Racickas")

# with open('08_darbas_su_failais/eilutes.txt', 'r', encoding='utf-8') as failas:
#     for eilute in failas:
#         print(eilute)
#         if "vėjas" in eilute.lower():
#             print(eilute)
#         else:
#             continue


# with open("eilutes.txt", "w", encoding="utf-8") as failas:
#     failas.write("Saulėlydis žėri žemę švelniai.\n")
#     failas.write("Vakare vėjas šnypščia medžius.\n")
#     failas.write("Vėjas nerimsta, šnypščia ir švilpia.\n")

# with open("eilutes.txt", "a", encoding="utf-8") as failas:
#     failas.write("Jūsų vardas ir pavardė\n")  # Čia įrašykite savo vardą ir pavardę

# with open("eilutes.txt", "r", encoding="utf-8") as failas:
#     for eilute in failas:
#         if "vėjas" in eilute:
#             print(eilute)
