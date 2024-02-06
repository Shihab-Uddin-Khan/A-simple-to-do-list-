def user_interface():
    print("---Welcome to your to-do list---")
    print("1. Enter new to-do list.\t 2. Search and manage to-do list.\t 3. Exit.\t")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        entry_to_do_list()
    elif choice == '2':
        search_and_manage_to_do_list()
    elif choice == '3':
        print("Exiting program. Goodbye!")
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
        user_interface()

def entry_to_do_list():
    date = input("Enter date for the to-do list (YYYY-MM-DD): ")
    tasks = input(f"Enter your to-do list for {date} (separate tasks with commas): ")

    with open("to_do_list.txt", "a") as file:
        file.write("{}: {}\n".format(date, tasks))

    print("To-do list added successfully!")
    user_interface()1
    

def search_and_manage_to_do_list():
    date = input("Enter date to search for to-do list (YYYY-MM-DD): ")

    try:
        with open("to_do_list.txt", "r") as file:
            lines = file.readlines()

        matching_lines = [line for line in lines if date in line]

        if matching_lines:
            matching_lines.sort(key=lambda x: int(x.split(":")[0]))

            for i, line in enumerate(matching_lines, start=1):
                print("{}. {}".format(i, line.strip()))

            edit_choice = input("Do you want to edit or expand a task? (yes/no): ").lower()

            if edit_choice == 'yes':
                edit_to_do_list(date, matching_lines)
            else:
                user_interface()
        else:
            print("No to-do lists found for the specified date.")
            user_interface()

    except FileNotFoundError:
        print("No to-do lists found.")
        user_interface()

def edit_to_do_list(date, matching_lines):
    try:
        with open("to_do_list.txt", "r") as file:
            lines = file.readlines()

        with open("to_do_list.txt", "w") as file:
            for line in lines:
                if date in line:
                    task_number = int(input("Enter the task number to edit: "))
                    new_task = input("Enter the new task: ")
                    matching_lines[task_number - 1] = "{}: {}\n".format(date, new_task)

            for line in lines:
                if line not in matching_lines:
                    file.write(line)

        print("To-do list edited successfully!")
        user_interface()

    except FileNotFoundError:
        print("No to-do lists found.")
        user_interface()

# Initial program execution
user_interface()