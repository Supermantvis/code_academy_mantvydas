# Define empty lists to store tasks and completed tasks
tasks = []
completed_tasks = []

# Display menu options and ask for input
while True:
    print("To-do List Menu:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Remove task")
    print("5. View completed tasks")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")

    # Add a task
    if choice == "1":
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added.\n")

    # View tasks
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks.\n")
        else:
            print("Tasks:")
            for i in range(len(tasks)):
                print(str(i+1) + ". " + tasks[i])
            print()

    # Mark task as completed
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks.\n")
        else:
            print("Tasks:")
            for i in range(len(tasks)):
                print(str(i+1) + ". " + tasks[i])
            task_index = int(input("Enter the number of the task you completed: "))
            if task_index < 1 or task_index > len(tasks):
                print("Invalid task number.\n")
            else:
                completed_task = tasks.pop(task_index-1)
                completed_tasks.append(completed_task)
                print("Task marked as completed.\n")

    # Remove a task
    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks.\n")
        else:
            print("Tasks:")
            for i in range(len(tasks)):
                print(str(i+1) + ". " + tasks[i])
            task_index = int(input("Enter the number of the task you want to remove: "))
            if task_index < 1 or task_index > len(tasks):
                print("Invalid task number.\n")
            else:
                del tasks[task_index-1]
                print("Task removed.\n")

    # View completed tasks
    elif choice == "5":
        if len(completed_tasks) == 0:
            print("No completed tasks.\n")
        else:
            print("Completed Tasks:")
            for i in range(len(completed_tasks)):
                print(str(i+1) + ". " + completed_tasks[i])
            print()

    # Exit the program
    elif choice == "6":
        print("Exiting...")
        break

    # Invalid input
    else:
        print("Invalid input. Please enter a number from 1 to 6.\n")
