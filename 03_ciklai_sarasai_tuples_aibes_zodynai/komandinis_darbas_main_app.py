import os

to_do_list = []
done_list = []
# in_progress_list = []
# in_review_list = []

os.system('cls')

while True:
    os.system('cls')
    print('-------[JIRA KNOCKOFF\'as]----------')
    print('-------[Uzduociu tvarkytuvas]----------')
    print('BACKLOG TASKS sarasas: ', to_do_list)
    print('DONE TASKS sarasas: ', done_list)
    print('Pasirinkite 1 jeigu norite prideti nauju uzduociu i to do list\'a')
    print('Pasirinkite 2 jeigu norite perkelti tasks is to_do_list i done_list')
    print('Pasirinkite 3 jeigu norite perkelti tasks is done_list i to_do_list')
    print('Pasirinkite 4 jeigu norite perkelti grizti i pagrindini meniu')
    pasirinkimas = input("Pasirinkite: ")


    if pasirinkimas == "1":
        os.system('cls')
        to_do_list.append(input("Irasykite uzduoti i to do list: "))
        print('BACKLOG sarasas: ', to_do_list)
        print('uzduotis irasyta i to do list\'a')
        print('')



    if pasirinkimas == "2":
        print('iseiname is programos.')
        break
