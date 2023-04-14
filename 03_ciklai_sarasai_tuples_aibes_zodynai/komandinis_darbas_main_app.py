import os

to_do_list = ['task1', 'task2']  # initial elements in list to for testing other menu options
done_list = ['task69']  # initial elements in list to for testing other menu options

# in_progress_list = []  # additional list for creating intermediate steps when moving tasks
# in_review_list = []  # additional list for creating intermediate steps when moving tasks


def print_lists():  # function to print both list's contents
    print('TO-DO LIST TASKS: ', to_do_list)
    print('DONE TASKS: ', done_list, '\n')


os.system('cls')  # clear screen (windows cli syntax)


while True:  # main menu loop
    os.system('cls')  # clear screen (windows cli syntax)
    print('----------[ JIRA KNOCKOFF :) ]----------\n')
    print_lists()  # function to print both list's contents
    print('Choose 1 if you want to add tasks to TO-DO LIST.')
    print('Choose 2 if you want to move tasks from TO-DO LIST to DONE_LIST.')
    print('Choose 3 if you want to move tasks from DONE_LIST to TO-DO LIST.')
    print('Choose 9 if you want to exit program.')
    choice_main_menu = input('Choose: ')  # main menu control options

    if choice_main_menu == '1':  # menu for adding tasks to TO-DO list
        while True:  # loop for adding multiple tasks
            os.system('cls')  # clear screen (windows cli syntax)
            print_lists()  # function to print both list's contents
            to_do_list.append(input('Add task to TO-DO LIST: '))  # tasks added to_do_list
            os.system('cls')  # clear screen (windows cli syntax)
            print_lists()  # function to print both list's contents
            print('Task inserted in TO-DO LIST.')
            print('Choose 1 if you want to add another task.')
            print('Choose 2 if you want to go back.')
            choice_1st_menu = input('Choose: ')  # 1st menu control options
            if choice_1st_menu == '2':  # choice to go back to main menu
                print('going back to main menu.')
                break


    if choice_main_menu == '2':  # menu for task moving from DONE to TO-DO 
        while True:
            os.system('cls')  # clear screen (windows cli syntax)
            print('TO-DO LIST TASKS: \n')
            print(f"{'NUMBER':<10} {'TASKS'}")  # string formating to add column names for 'task index' & 'task name'
            for i, task in enumerate(to_do_list):
                # print(i, task)  # simple in code / non descriptive in terminal
                print("{:<10} {}".format(i, task))  # formated & descriptive in terminal / harder to read as code
            print('\n')
            task_id = int(input(f"Choose task \033[32mnumber\033[0m from TO-DO LIST you wish to transfer to DONE_LIST: "))  # user imput choosing task to move
            done_list.append(to_do_list[task_id])  # move task from to_do_list to done_list
            del to_do_list[task_id]  # delete task from to_do_list since it's moved to done_list
            os.system('cls')  # clear screen (windows cli syntax)
            print('Task moved to DONE_LIST.\n')
            print_lists()  # function to print both list's contents
            print('Choose 1 if you move another task.')
            print('Choose 2 if you want to go back.')
            choice_2nd_menu = input('Choose: ')  # 2nd menu control options
            if choice_2nd_menu == '2':  # choice to go back to main menu
                print('going back to main menu.')
                break


    if choice_main_menu == '3':  # menu for task moving from DONE_LIST to TO-DO LIST 
        while True:
            os.system('cls')  # clear screen (windows cli syntax)
            print('DONE_LIST TASKS: \n')
            print(f"{'NUMBER':<10} {'TASKS'}")  # string formating to add column names for 'task index' & 'task name'
            for i, task in enumerate(done_list):
                # print(i, task)  # simple in code / non descriptive in terminal
                print("{:<10} {}".format(i, task))  # formated & descriptive in terminal / harder to read as code
            print('\n')
            task_id = int(input(f"Choose task \033[32mnumber\033[0m from DONE_LIST you wish to transfer to TO-DO LIST: "))  # user imput choosing task to move
            to_do_list.append(done_list[task_id])  # move task from done_list to to_do_list
            del done_list[task_id]  # delete task from done_list since it's moved to to_do_list
            os.system('cls')  # clear screen (windows cli syntax)
            print('Task moved to DONE_LIST.\n')
            print_lists()  # function to print both list's contents
            print('Choose 1 if you move another task.')
            print('Choose 2 if you want to go back.')
            choice_3nd_menu = input('Choose: ')  # 3rd menu control options
            if choice_3nd_menu == '2':  # choice to go back to main menu
                print('going back to main menu.')
                break


    if choice_main_menu == '9':  # menu for program termination
        print('Exiting program..')
        break
