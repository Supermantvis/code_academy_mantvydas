'''
************************PROGRAMOS APRASYMAS************************
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

'''
PAPILDYMAS 1:
Naudojant json:
paleidus programą, jeigu randamas šaldytuvo json failas, jį nuskaityti ir užpildyti šaldytuvą jo turiniu.
Uždarant programą, atnaujinti šaldytuvo json failo turinį esamu šaldytuvo turiniu.
'''

'''
PAPILDYMAS 2:
Patobulinkite savo šaldytuvo programą:

Gaudykite visas galimas vartotojo sąsajos klaidas, ypač įvedant kiekius.
Šaldytuvo saugojimo į failą/ištraukimo iš failo klaidų gaudymą galite įgyvendinti per try except.
Sukurkite loggerį, kuris į failą kauptų informaciją apie įdėtus ir išimtus produktus su kiekiais, ir veiksmo data/laiku.
'''
import logging
import json
import os
import os.path

logging.basicConfig(
    filename='./04_funkcijos/saldytuvo_logeris.log', 
    encoding='UTF-8', 
    level=logging.INFO,
    format='TIME: %(asctime)s; LOGGER NAME: %(name)s; LOG LEVEL: %(levelname)s; MESSAGE: %(message)s; LINE NO: %(lineno)d; FUNCTION: %(funcName)s'
)

path = '04_funkcijos/saldytuvo_turinys.json'
check_file = os.path.isfile(path)
products = {}

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def json_i_saldytuva():
    # paleidus programą, jeigu randamas šaldytuvo json failas, jį nuskaityti ir užpildyti šaldytuvą jo turiniu
    if check_file:
        with open("04_funkcijos/saldytuvo_turinys.json", "r", encoding="utf-8") as f:
            products = json.load(f)
            return products

products = json_i_saldytuva()

def saldytuvas_i_json():
    # Uždarant programą, atnaujinti šaldytuvo json failo turinį esamu šaldytuvo turiniu.
    with open("04_funkcijos/saldytuvo_turinys.json", "w", encoding="utf-8") as f:
        json.dump(products, f)

def view_product_list(item_dict):  # Karolis Venckus
    print("Product List:")
    for item_name, item_weight in item_dict.items():
        print(f"{item_name}: {item_weight}")

def remove_if_zero(item_dict):   # Karolis Venckus
    empty_products = [product for product, details in item_dict.items() if details == 0]
    for product in empty_products:
        del item_dict[product]
    if empty_products:
        print(f"{', '.join(empty_products)} removed from the product list.")

def add_product(product_dict, product_name, count):  # Karolis Jasadavičius
    try:
        count = float(count)
        product_dict[product_name] += count
    except ValueError as ve:
        print(f"{count}, not a number")
        logging.info(f"{count}, not a number. {ve}")
    except KeyError as ke:
        product_dict[product_name] = count
        print(f"{product_name} count added successfully")
        logging.info(f"product: {product_name} has been added. ammount {count}. this is key error: {ke}")
    else:
        print(f"{product_name} count updated successfully")
        logging.info(f"Existing product count changed to: {product_dict[product_name]}.")

# def remove_product(product_dict, product_name, count_reduce=0):  # BBZ try except shit ....
#     try:
#         count_reduce = float(count_reduce)
#         if count_reduce == 0:
#             del product_dict[product_name]
#             print(f"{product_name} removed successfully")
#     except:

#         else:
#             product_dict[product_name] -= count_reduce
#             print(f"{product_name} count lowered by {count_reduce} (Removed if reaches 0)")
#             remove_if_zero(products)
#     else:
#         print(f"{product_name} is not in the fridge")

def remove_product(product_dict, product_name, count_reduce=0): # Karolis Jasadavičius
    if product_name in product_dict:
        if count_reduce == 0:
            del product_dict[product_name]
            print(f"{product_name} removed successfully")
        else:
            product_dict[product_name] -= count_reduce
            print(f"{product_name} count lowered by {count_reduce} (Removed if reaches 0)")
            remove_if_zero(products)
    else:
        print(f"{product_name} is not in the fridge")

def calculate_fridge_mass(products):  # Milda Auglytė
    products_list = list(products.values())
    items_kg = 0
    for item in products_list:
        items_kg = items_kg + item
    return items_kg

def check_recipe(products):  # Karolis Venckus, Karolis Jasadavičius
    recipe = input("Enter the recipe in the format 'ingredient: quantity' (e.g. 'apple: 2'):\n")
    recipe_dict = {}
    for item in recipe.split(','):
        item_list = item.split(':')
        recipe_dict[item_list[0].strip()] = float(item_list[1].strip())
    max_servings = min([
    int(products[item] // quantity) # Calculate how many servings can be made with each ingredient
    for item, quantity in recipe_dict.items() # Only consider ingredients that are in the fridge
    if item in products
])
    missing_items = {}
    for item, quantity in recipe_dict.items():
        if item not in products:
            missing_items[item] = quantity
        elif products[item] < quantity:
            missing_items[item] = products[item] - quantity
    if max_servings == 0 or missing_items:
        print(f"You can't make any servings, you don't have enough ingredients")
        print("You are missing the following ingredients:")
        for item, quantity in missing_items.items():
            print(f"{item}:{abs(quantity)}")
        return
    else:
        print(f"You can make up to {max_servings} servings with the ingredients you have.")
    servings = int(input("Enter the number of servings:\n"))
    if servings > max_servings:
        print(f"Can't make more than {max_servings} servings, not enough ingredients")
        return
    elif not len(missing_items) > 0:
        print("You have enough ingredients to make this recipe.")
        print(f"You used No. of {servings} servings of the following ingredients:")
        for item, quantity in recipe_dict.items():
            print(f"{item}: {quantity * servings:.2f}")
        for item, quantity in recipe_dict.items():
            products[item] -= quantity * servings

while True:
    os.system('cls')
    print('----------[ FRIDGE ]----------\n')
    print('Choose 1 if you want to view product list')
    print('Choose 2 if you want to add product.')
    print('Choose 3 if you want to remove product.')
    print('Choose 4 if you want to count total mass of products.')
    print('Choose 5 if you want to check recipies.')
    print('Choose 9 if you want to close the fridge.')
    choice_main_menu = input('Choose: ')

    if choice_main_menu == '1':  # view product list
        os.system('cls')
        remove_if_zero(products)
        view_product_list(products)
        input('Smash ENTER to continue: ')

    elif choice_main_menu == '2':  # add product
        os.system('cls')
        added_product = input("Enter product name you wish to add: ")
        product_count = input("Enter the amount you are adding: ")
        add_product(products, added_product, product_count)
        input('Smash ENTER to continue: ')

    elif choice_main_menu == '3':  # remove product
        os.system('cls')
        product_name = input("Enter product name you wish to take: ")
        deleting = input("Choose your option\n 1: Take all \n 2: Ammount\n")
        if deleting == '2':
            product_count = float(input("Enter the amount you are taking: "))
            remove_product(products, product_name, count_reduce=product_count)
        else:
            remove_product(products, product_name, count_reduce=0)
        input('Smash ENTER to continue: ')

    elif choice_main_menu == '4':  # count total mass of products.
        os.system('cls')
        print('\033[96mTotal fridge mass:\033[0m', calculate_fridge_mass(products))  # Milda Auglytė
        input('smash ENTER to continue: ')

    elif choice_main_menu == '5':  # recipe check.
        os.system('cls')
        print('RECIPE CHECKING: ')
        check_recipe(products)
        input('Smash ENTER to continue: ')

    elif choice_main_menu == '9':
        saldytuvas_i_json()
        print('Closing fridge..')
        break
