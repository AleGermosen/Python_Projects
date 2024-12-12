### To Do List App

# Create a menu
# Add, view and remove tasks

list_tasks = []

# Define functions
def add_task(user_choice):
    list_tasks.append(user_choice)
    print(f"Task '{user_choice}' added.")

def remove_task(user_choice):
    try:
        list_tasks.pop(int(user_choice) - 1)
        print(f"Task {user_choice} removed.")
    except (IndexError, ValueError):
        print("Invalid task number.")

def view_tasks():
    if not list_tasks:
        print("No tasks to display.")
    else:
        print("Tasks:")
        for index, task in enumerate(list_tasks, start=1):
            print(f"{index}. {task}")

# Create a dictionary mapping user choices to functions
menu_dict = {
    "1": view_tasks,
    "2": add_task,
    "3": remove_task,
    "4": exit,
}

# Main menu function
def to_do_list():
    while True:
        print("""
To-Do List Menu:
1. View tasks
2. Add a task
3. Remove a task
4. Exit       
        """)
        user_input = input("Enter your choice: ").strip()

        if user_input in menu_dict:
            if user_input in ["2", "3"]:  # For options that require input
                task_input = input("Enter the task: ").strip()
                menu_dict[user_input](task_input)
            else:
                menu_dict[user_input]()  # Call the function directly
        else:
            print("Invalid choice. Please try again.")

# Run the menu
to_do_list()