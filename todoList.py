
tasks = {}

while True:
    print("TO-DO LIST")
    print("Choose an Option:")
    print("1. To Create a Task")
    print("2. To Update a Task")
    print("3. To Track Tasks")
    print("4. To Quit")

    choose = input("Enter your choice: ")

    if choose == "1":
        # To create a new task
        tskName = input("Enter task name: ")
        if tskName not in tasks:
            tasks[tskName] = False
            print(f"Task '{tskName}' created successfully!")
        else:
            print(f"Task '{tskName}' already exists!")

    elif choose == "2":
        # Update the status of a task
        tskName = input("Enter task name: ")
        if tskName in tasks:
            tasks[tskName] = not tasks[tskName]
            print(f"Task '{tskName}' updated successfully!")
        else:
            print(f"Task '{tskName}' not found!")

    elif choose == "3":
        # Display all tasks
        print("To-Do List:")
        for task, status in tasks.items():
            status_str = "Done" if status else "Not Done"
            print(f"{task}: {status_str}")

    elif choose == "4":
        # Quit the application
        break

    else:
        print("Invalid Choice. Please try again.")