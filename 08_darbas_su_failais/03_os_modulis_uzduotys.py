'''
Pirma užduotis
Sukurkite naują katalogą pavadinimu "Mano_Katalogas" dabartinėje darbo vietoje. Patikrinkite, ar katalogas buvo sėkmingai sukurtas, ir atspausdinkite rezultatą.
'''
# import os

# katalogo_kelias = './08_darbas_su_failais/Mano_Katalogas'
# if not os.path.exists(katalogo_kelias):
#     os.makedirs(katalogo_kelias)
#     print(f"Katalogas '{katalogo_kelias}' sukurtas.")
# else:
#     print(f"Katalogas '{katalogo_kelias}' jau egzistuoja.")


# SUGGESTED SOLUTION:
# katalogo_kelias = "Mano_Katalogas"

# if not os.path.exists(katalogo_kelias):
#     os.makedirs(katalogo_kelias)
#     print(f"Katalogas '{katalogo_kelias}' sukurtas.")
# else:
#     print(f"Katalogas '{katalogo_kelias}' jau egzistuoja.")
'''
Antra užduotis
Parašykite programą, kuri peržiūrėtų dabartinį darbo katalogą ir atspausdintų visus rastus failus bei katalogus.
'''
# import os

# katalogo_kelias = './08_darbas_su_failais'
# if os.path.exists(katalogo_kelias):
#     print(os.listdir(katalogo_kelias))
# else:
#     print('nera tokio katalogo')


# SUGGESTED SOLUTION:
# dabartinis_katalogas = os.getcwd()
# print(f"Dabartinis katalogas: {dabartinis_katalogas}")

# print("Failai ir katalogai:")
# for elementas in os.listdir(dabartinis_katalogas):
#     print(elementas)
'''
Trečia užduotis
Sukurkite naują failą pavadinimu "testas.txt" dabartinėje darbo vietoje. Tada parašykite programą, kuri patikrintų, ar failas "testas.txt" egzistuoja, ir trintų jį, jei egzistuoja. Atspausdinkite rezultatą, kad failas buvo sėkmingai ištrintas.
'''
# import os

# with open("./08_darbas_su_failais/testas.txt", "w") as failas:
#     failas.write('belekoks tekstas lalalala ..,.,.,.. :))')
#     print(f"Failas \"testas.txt\" sukurtas!")

# failo_kelias = './08_darbas_su_failais/testas.txt'

# if os.path.exists(failo_kelias):
#     os.remove(failo_kelias)
#     print(f"Failas '{failo_kelias}' istrintas.")
# else:
#     print(f"Failas '{failo_kelias}' neegzistuoja.")


# SUGGESTED SOLUTION:
# failo_kelias = "testas.txt"

# # Sukurkite failą
# with open(failo_kelias, "w") as f:
#     f.write("Tai yra testinis failas.")

# # Patikrinkite, ar failas egzistuoja, ir trinkite jį
# if os.path.exists(failo_kelias):
#     os.remove(failo_kelias)
#     print(f"Failas '{failo_kelias}' ištrintas.")
# else:
#     print(f"Failas '{failo_kelias}' neegzistuoja.")