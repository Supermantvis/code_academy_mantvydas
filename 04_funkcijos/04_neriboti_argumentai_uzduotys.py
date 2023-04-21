'''
Pirma užduotis
Parašykite funkciją, kuri grąžina didžiausią *args elemento reikšmę.
'''

# def biggest_value(*args):
#     print(max(args))

# biggest_value(1, 2, 90, 3)


# def didziausias(*args):  # SUGGESTED SOLUTION
#     if len(args) == 0:
#         return None
#     didziausia_reiksme = args[0]
#     for arg in args:
#         if arg > didziausia_reiksme:
#             didziausia_reiksme = arg
#     return didziausia_reiksme

# print(didziausias(1, 2, 90, 3))

'''
Antra užduotis
Parašykite funkciją, kuri grąžina tik **kwargs elemento raktus, kurie yra nurodyti šiame funkcijos kvietime:

print(raktai(vardas="Jonas", amzius=30, miestas="Vilnius"))
# kvietime galite nurodyti tik vardą, amžių bei miestą, kad grąžintų:
{'vardas': 'Jonas', 'amzius': 30, 'miestas': 'Vilnius'}
'''

# def raktai(**kwargs):
#     for key, _ in kwargs.items():
#         print(f"Tik raktas: {key}")


# raktai(vardas="Jonas", amzius=30, miestas="Vilnius")


# def raktai(**kwargs):  # SUGGESTED SOLUTION
#     nurodyti_raktai = {}
#     for key in kwargs:
#         if key in ["vardas", "amzius", "miestas", "metai"]:
#             nurodyti_raktai[key] = kwargs[key]
#     return nurodyti_raktai

# print(raktai(vardas="Jonas", amzius=30, miestas="Vilnius", metai=2023))  # {'vardas': 'Jonas', 'amzius': 30, 'miestas': 'Vilnius'}
# print(raktai(pavadinimas="Python"))  # {}


'''
Trečia užduotis
Parašykite funkciją, kuri sujungia *args sąrašą ir **kwargs reikšmes į vieną sarašą.
'''

# def raktai(*args, **kwargs):
#     sarasiukas = []
#     for arg in args:
#         sarasiukas.append(arg)
#     for key, value in kwargs.items():
#         sarasiukas.append(value)
#     return sarasiukas


# def raktai(*args, **kwargs):  # SUGGESTED SOLUTION
#     visi_elementai = list(args)
#     visi_elementai += list(kwargs.values())
#     return visi_elementai

# print(raktai("Jonas", "linksmas", "draugiškas", "drąsus", vardas="Jonas", amzius=30, miestas="Vilnius"))