tasks =[]
while True:
    print("to do list")
    print("1.add task")
    print("2.view task")
    print("3.delete tasks")
    print("4.exit")

    choice = input("enter your choice ")
    if choice == '1':
        task = input("enter your task ")
        tasks.append(task)

    elif choice == '2':
        if not tasks:
            print("no tasks available")
        else:
            print("your tasks are")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
    elif choice == '3':
        if not tasks:
            print("no tasks to delete ")
        else:
            for i,task in enumerate(tasks,start=1):
                print(f'{i}. {task}')
            num = int(input('enter task number to delete: '))
            if 1<= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f"'{removed}' deleted successfully!")
            else:
                print("invalid task number ")
    elif choice == '4':
        print("goodbye")
        break
    else:
        print("invalid choice ")
            
