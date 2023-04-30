'''
Pirma užduotis
Sukurkite klasę Studentas su atributais vardas, pavarde ir amzius. Pridėkite tris metodus:

pilnas_vardas(): Grąžina pilną studento vardą, naudojant @property dekoratorių.
ar_pilnametis(): Grąžina True, jei studento amžius yra didesnis arba lygus 18, ir False, jei ne. Naudokite @staticmethod dekoratorių.
sukurti_studenta(cls, vardas: str, pavarde: str, amzius: int): Grąžina naują Studentas objektą. Naudokite @classmethod dekoratorių.
Sukurkite keletą studentų objektų, naudojant klasės metodą sukurti_studenta(), ir išbandykite visus metodus.
'''
# class Studentas():
#     def __init__(self, vardas, pavarde, amzius):
#         self.vardas = vardas
#         self.pavarde = pavarde
#         self.amzius = amzius
    
#     @property
#     def pilnas_vardas(self):
#         return f"{self.vardas} {self.pavarde}"
    
#     @staticmethod
#     def ar_pilnametis(amzius):
#         if amzius >= 18:
#             return True
#         else:
#             return False
    
#     @classmethod
#     def sukurti_studenta(cls, vardas: str, pavarde: str, amzius: int):
#         return cls(vardas, pavarde, amzius)

# # studento_inicialai = Studentas('Tomas', 'Tomaitis', 19)
# # print(studento_inicialai.ar_pilnametis(22))

# studentas1 = Studentas.sukurti_studenta('Jonas', 'Jonaitis', 17)
# studentas2 = Studentas.sukurti_studenta('Petras', 'Petraitis', 22)

# print(Studentas.ar_pilnametis(studentas1.amzius))
# print(Studentas.ar_pilnametis(studentas2.amzius))


'''
Antra užduotis
Parašykite dekoratorių, kuris:

visus dekoruotos funkcijos tekstinius argus ir kwargus paverčia didžiosiomis raidėmis.
visus funkcijos teksinius rezultatus paverčia didžiosiomis raidėmis.
'''
def kazkokia_funk(funkcija):
    def wrapper(*args, **kwargs):
        if all((type(arg) == str) for arg in args):
            rezultatas = funkcija(*args, **kwargs)
        else:
            raise ValueError("Klaida: visi argumentai turi būti str formatu")
        return rezultatas

    return wrapper

@kazkokia_funk
def didinimas(*args):
    listas = []
    for arg in args:
        listas.append(arg.upper())
    return listas

print(didinimas('adadasas', 'cbasjcbja', 'hbwjnwadvbhjn'))


# SUGGESTED SOLUTION: 
from functools import wraps
def make_upper(func):
    """ This decorator makes all function arguments and keyword arguments upper case if they are text, then makes the result upper case if it is text """
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if type(arg) == str:
                arg = arg.upper()
        for kwarg in kwargs:
            if type(kwarg) == str:
                kwargs[kwarg] = kwargs[kwarg].upper()
        result = func(*args, **kwargs)
        if type(result) == str:
            result = result.upper()
        return result
    return wrapper

# testing the above decorator with function, which makes text lowecase, with a debug print
@make_upper
def make_lower(string="Hello World"):
    print(f"making '{string}' lowercase")
    return string.lower()

# testing of the decorated function
print(make_lower())
print(make_lower("it works!"))