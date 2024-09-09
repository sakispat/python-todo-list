tasks = []


def add_task(task):
    tasks.append(task)
    print(f'{ task } has been added.')


def view_tasks():
    if tasks:
        for index, task in enumerate(tasks, start=1):
            print(f'{ index }. { task }')
    else:
        print('No tasks to display!')


def remove_task(index):
    if 0 <= index <= len(tasks):
        removed = tasks.pop(index)
        print(f'{ removed } has been removed.')
    else:
       print('Invalid index!')


while True:
    print('\n**********************************')
    print('*            Options             *')
    print('**********************************\n')
    print('1. Add task\n2. View tasks\n3. Remove task\n4. Exit')
    choice = input("Choose an option: ")
    print()

    match choice:
        case '1':
            task = input('Enter a new task: ')
            add_task(task)
        case '2':
            view_tasks()
        case '3':
            index = int(input('Enter the task number to remove: ')) - 1
            remove_task(index)
        case '4':
            break
        case _:
            print('Invalid choice, please try again.')
