tasks = []

print("The To-Do List App")

while True:
    print("/nWhat would you like to do?")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Exit")

    choice = input("Enter your choice")

    if choice == '1':
        if tasks == []:
            print("No tasks found.")
        else:
            i = 1
            for task in tasks:
                print(str(i) + " " + task)

    elif choice == '2':
        new = input("Type your task: ")
        if new != "":
            tasks.append(new)
            print("New task has been added.")
        else:
            print("You must enter something.")

    elif choice == '3':
        if len(tasks) == 0:
            print("Nothing to be delete.")
        else:
            number = input("Enter the number of the task to remove: ")
            if number.isdigit():
                number = int(number)
                if number > 0 and number <= len(tasks):
                    gone = tasks.pop(number - 1)
                    print("Deleted:", gone)
                else:
                    print("Number is out of range.")
            else:
                print("That is not a number.")

    elif choice == '4':
        print("Exit.")
        break

    else:
        print(" Invalid.. please try again.")
