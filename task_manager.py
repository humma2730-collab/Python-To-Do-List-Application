from storage import save_tasks
from views import view_tasks

# Add New Task
def add_task(tasks):

    title = input("Enter Task Name: ").strip()

    if title == "":
        print("❌ Task Name Cannot Be Empty!\n")
        return

    print("\nSelect Priority")
    print("1. High")
    print("2. Medium")
    print("3. Low")

    choice = input("Enter Choice: ")

    if choice == "1":
        priority = "High"
    elif choice == "2":
        priority = "Medium"
    elif choice == "3":
        priority = "Low"
    else:
        priority = "Medium"

    due_date = input("Enter Due Date (DD-MM-YYYY): ").strip()

    task = {
        "title": title,
        "status": "Pending",
        "priority": priority,
        "due_date": due_date
    }
    tasks.append(task)
    save_tasks(tasks)
    print("\n✅ Task Added Successfully!\n")

# Edit Task
def edit_task(tasks):

    view_tasks(tasks)

    if not tasks:
        return
    try:
        number = int(input("Enter Task Number To Edit: "))
        if 1 <= number <= len(tasks):
            task = tasks[number - 1]
            title = input(
                f"New Title ({task['title']}): ").strip()
            if title != "":
                task["title"] = title

            print("\nSelect Priority")
            print("1. High")
            print("2. Medium")
            print("3. Low")
            print("Press Enter To Keep Previous")

            priority = input("Enter Choice: ").strip()

            if priority == "1":
                task["priority"] = "High"
            elif priority == "2":
                task["priority"] = "Medium"
            elif priority == "3":
                task["priority"] = "Low"
            due = input(
                f"New Due Date ({task['due_date']}): ").strip()
            if due != "":
                task["due_date"] = due
            save_tasks(tasks)
            print("\n✅ Task Updated Successfully!\n")
        else:
            print("\n❌ Invalid Task Number!\n")

    except ValueError:
        print("\n❌ Please Enter Numbers Only!\n")


# Delete Task
def delete_task(tasks):

    view_tasks(tasks)

    if not tasks:
        return
    try:
        number = int(input("Enter Task Number To Delete: "))
        if 1 <= number <= len(tasks):
            deleted = tasks.pop(number - 1)
            save_tasks(tasks)
            print(f"\n✅ '{deleted['title']}' Deleted Successfully!\n")
        else:
            print("\n❌ Invalid Task Number!\n")
    except ValueError:
        print("\n❌ Please Enter Numbers Only!\n")

# Mark Completed
def mark_completed(tasks):

    view_tasks(tasks)
    if not tasks:
        return
    try:
        number = int(input("Enter Task Number: "))
        if 1 <= number <= len(tasks):
            tasks[number - 1]["status"] = "Completed"
            save_tasks(tasks)
            print("\n✅ Task Marked As Completed!\n")
        else:
            print("\n❌ Invalid Task Number!\n")

    except ValueError:
        print("\n❌ Please Enter Numbers Only!\n")

# Search Task
def search_task(tasks):

    if not tasks:
        print("\n❌ No Tasks Found!\n")
        return
    keyword = input("Enter Task Name To Search: ").strip().lower()
    found = False

    print("\n****** SEARCH RESULT *******\n")

    for index, task in enumerate(tasks, start=1):

        if keyword in task["title"].lower():

            print(f"{index}. {task['title']}")
            print(f"Status   : {task['status']}")
            print(f"Priority : {task['priority']}")
            print(f"Due Date : {task['due_date']}")
            print("-" * 35)

            found = True

    if not found:
        print("❌ No Matching Task Found!")

    print()
    # Sort Tasks
def sort_tasks(tasks):

    if not tasks:
        print("\n❌ No Tasks Found!\n")
        return

    print("\n*******  SORT TASKS *******")
    print("1. Sort By Priority")
    print("2. Sort By Due Date")
    print("3. Sort By Status")

    choice = input("Enter Your Choice: ")

    if choice == "1":

        priority_order = {
            "High": 1,
            "Medium": 2,
            "Low": 3
        }

        tasks.sort(key=lambda task: priority_order.get(task["priority"], 4))

        print("\n✅ Tasks Sorted By Priority Successfully!\n")

    elif choice == "2":

        tasks.sort(key=lambda task: task["due_date"])

        print("\n✅ Tasks Sorted By Due Date Successfully!\n")

    elif choice == "3":

        status_order = {
            "Pending": 1,
            "Completed": 2
        }

        tasks.sort(key=lambda task: status_order.get(task["status"], 3))

        print("\n✅ Tasks Sorted By Status Successfully!\n")

    else:
        print("\n❌ Invalid Choice!\n")
        return

    save_tasks(tasks)