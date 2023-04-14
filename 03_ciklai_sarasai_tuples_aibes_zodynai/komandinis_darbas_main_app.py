import os

backlog_list = []
done_list = []
# in_progress_list = []
# in_review_list = []

os.system('cls')

while True:   # PRADINIS PROGRAMOS VEIKIMO LYGIS
    os.system('cls')
    print('-------[JIRA KNOCKOFF\'as]----------')
    print('Pasirinkite 1 jeigu norite dirbti su uzduociu tvarkymu')
    print('Pasirinkite 2 jeigu norite iseiti is programos')

    pasirinkimas = input("Pasirinkite: ")
    if pasirinkimas == "1":
        while True:  # UZDUOCIU TVARKYMO LYGIS
            os.system('cls')
            print('-------[Uzduociu tvarkymas]----------')
            print('Pasirinkite 1 jeigu norite prideti nauju uzduociu i backlog\'a')
            print('Pasirinkite 2 jeigu norite perkelti tasks is backlog_list i done_list')
            print('Pasirinkite 3 jeigu norite perkelti tasks is done_list i backlog_list')
            print('Pasirinkite 4 jeigu norite perkelti grizti i pagrindini meniu')
            pasirinkimas = input("Pasirinkite: ")

            if pasirinkimas == "1":
                backlog_list.append(input("Irasykite uzduoti: "))
                print('BACKLOG sarasas: ', backlog_list)


            if pasirinkimas == "2":
                print('griztame i pagrindini meniu.')
                break


    if pasirinkimas == "2":
        print('iseiname is programos.')
        break
