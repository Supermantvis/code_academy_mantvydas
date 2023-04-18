'''
Parašykite programą šaldytuvas, kuri:
- saugo produktus žodyne, kur:
-- produkto pavadinimas yra raktas
-- kiekis yra reikšmė float
Tarkime, kad:
- kieti produktai matuojami kilogramais
- skysti litrais
- paruošti patiekalai matuojami vienetais
tokiu atveju, mums nereikia apibrėžti mato vieneto
Šaldytuvas turi meniu, per kurį galime:
- įdėti produktus
- išimti produktus
-- jeigu produkto kiekis tampa 0, ištriname
- peržiūrėti produktų sąrašą
- suskaičiuoti šaldytuvo turinio svorį
-- skystų tankis = 1
-- paruoštų patiekalų porcija sveria 1kg
BONUS:
Įterpti meniu punktą "ar išeina", kur vartotojo prašo įvesti:
- vienos porcijos receptą
-- įvedimo formatas: "ingredientas: kiekis" vienoje eilutėje.
- porcijų kiekį
Tada programa turėtų:
- išvesti, ar užtenka ingredientų patiekalams paruošti
- jeigu neužtenka, išvardinti ko ir kiek trūksta (shopping list).
- išvesti, kelioms porcijoms užtenka ingredientų, jei yra perteklius
'''

import time
import os

solid_products = {}
liquid_products = {}
meals = {}
products = {'milk': 2, 'fish': 5, 'beer': 4}
products_list = list(products.values())
# print(fridge_items)

def calculate_fridge_mass(products_list):
    items_mass = 0
    for item in products_list:
        items_mass = items_mass + item
    return items_mass

def add_product(product_name, count):
    # add products, 
    # if product is solid unit == kg
    # if product is solid unit == litres (l)
    pass

def remove_product(product_name, count):
    # product count reduce
    pass

def remove_if_zero():
    # this probably should run after remove_product() eg. if product == 'cheese': 0 ....
    pass

def calculate_fridge_mass(products):
    products_list = list(products.values())
    items_kg = 0
    for item in products_list:
        items_kg = items_kg + item
    return items_kg

while True:
    os.system('cls')
    print('----------[ FRIDGE ]----------\n')
    view_product_list()
    print('Choose 1 if you want to view product list')
    print('Choose 2 if you want to add product.')
    print('Choose 3 if you want to remove product.')
    print('Choose 4 if you want to count total mass of products.')
    print('Choose 9 if you want to exit program.')
    choice_main_menu = input('Choose: ')

    if choice_main_menu == '1':
        # while True:
        os.system('cls')
        print('Here will be product list')
        view_product_list()
        input('smash ENTER to continue: ')


    if choice_main_menu == '2':
        os.system('cls')
        print('Here will be product adding')
        input('smash ENTER to continue: ')

    if choice_main_menu == '3':
        os.system('cls')
        print('Here will be product removing')
        input('smash ENTER to continue: ')

    if choice_main_menu == '4':
        os.system('cls')
        print('Total fridge mass: ', calculate_fridge_mass(products))
        input('smash ENTER to continue: ')

    if choice_main_menu == '9':
        print('Exiting program..')
        break
