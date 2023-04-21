import os

# Create empty lists for tasks and done tasks
tasks = []
done_tasks = []

# Define a function to display the menu
def display_menu():
    print("Menu:")
    print("1. Add task")
    print("2. Remove task")
    print("3. Mark task as done")
    print("4. View tasks")
    print("5. View done tasks")
    print("6. Save tasks to file")
    print("7. Exit program")

# Define a function to add a task to the list
def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added.")

# Define a function to remove a task from the list
def remove_task():
    task = input("Enter task to remove: ")
    if task in tasks:
        tasks.remove(task)
        print("Task removed.")
    else:
        print("Task not found.")

# Define a function to mark a task as done
def mark_task_done():
    task = input("Enter task to mark as done: ")
    if task in tasks:
        tasks.remove(task)
        done_tasks.append(task)
        print("Task marked as done.")
    else:
        print("Task not found.")

# Define a function to display the tasks
def view_tasks():
    if len(tasks) == 0:
        print("No tasks.")
    else:
        print("Tasks:")
        for task in tasks:
            print("- " + task)

# Define a function to display the done tasks
def view_done_tasks():
    if len(done_tasks) == 0:
        print("No done tasks.")
    else:
        print("Done tasks:")
        for task in done_tasks:
            print("- " + task)

# Define a function to save tasks to a text file
def save_tasks_to_file():
    if len(tasks) == 0:
        print("No tasks to save.")
    else:
        file_name = input("Enter file name: ")
        with open(file_name + ".txt", "w") as f:
            for task in tasks:
                f.write(task + "\n")
        print("Tasks saved to file.")

# Clear the terminal
os.system("cls" if os.name == "nt" else "clear")

# Display the menu initially
display_menu()

# Loop until the user chooses to exit the program
while True:
    # Get the user's choice
    choice = input("Enter choice (1-7): ")
    
    # Clear the terminal
    os.system("cls" if os.name == "nt" else "clear")
    
    # Handle the user's choice
    if choice == "1":
        add_task()
    elif choice == "2":
        remove_task()
    elif choice == "3":
        mark_task_done()
    elif choice == "4":
        view_tasks()
    elif choice == "5":
        view_done_tasks()
    elif choice == "6":
        save_tasks_to_file()
    elif choice == "7":
        print("Exiting program...")
        break
    else:
        print("Invalid choice.")
    
    # Display the menu again
    display_menu()

# Clear the terminal
os.system("cls" if os.name == "nt" else "clear")

# Print a message indicating that the program has exited
print("Program exitedsS.")