import os

backlog_list = []
done_list = []
# in_progress_list = []
# in_review_list = []


os.system('clear')
while len(backlog_list) <= 3:
    print("-------[JIRA KNOCKOFF'as]----------")
    new_task = input('irasykite nauja uzduoti: ')
    backlog_list.append(new_task)

    print(backlog_list)







while True:
   
    print("-------[ Mūsų uber programėlė ]----------")
    print("1: aidas")
    print("0: išeiti")
    pasirinkimas = input("Pasirinkite: ")
    if pasirinkimas == "0":
        break
    if pasirinkimas == "1":
        tekstas = input("Šaukite: ")
        print((tekstas+" ") * 3)
        input("paspauskite ENTER kad tęsti...")