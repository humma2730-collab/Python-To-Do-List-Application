from storage import load_tasks
from task_manager import (
    add_task,
    edit_task,
    delete_task,
    mark_completed,
    search_task,
    sort_tasks
)

from views import (
    view_tasks,
    pending_tasks,
    completed_tasks,
    task_statistics
)


def menu():
    print("\n" + "*" * 45)
    print(" TO-DO LIST APPLICATION")
    print("*" * 45)
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Edit Task")
    print("4. Delete Task")
    print("5. Mark Task Completed")
    print("6. View Pending Tasks")
    print("7. View Completed Tasks")
    print("8. Search Task")
    print("9. View Statistics")
    print("10. Sort Tasks")
    print("11. Exit")
    print("*" * 45)

def main():
    tasks = load_tasks()
    while True:
        menu()
        try:
            choice = int(input("Enter Your Choice: "))
            if choice == 1:
                add_task(tasks)
            elif choice == 2:
                view_tasks(tasks)
            elif choice == 3:
                edit_task(tasks)
            elif choice == 4:
                delete_task(tasks)
            elif choice == 5:
                mark_completed(tasks)
            elif choice == 6:
                pending_tasks(tasks)
            elif choice == 7:
                completed_tasks(tasks)
            elif choice == 8:
                search_task(tasks)
            elif choice == 9:
                task_statistics(tasks)
            elif choice == 10:
                sort_tasks(tasks)
            elif choice == 11:
                print("\n❤️ Thank You For Using To-Do List Application!")
                print("👋 Goodbye!\n")
                break

            else:
                print("\n❌ Invalid Choice! Please Try Again.\n")

        except ValueError:
            print("\n❌ Please Enter Numbers Only!\n")


if __name__ == "__main__":
    main()