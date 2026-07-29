# View All Tasks
def view_tasks(tasks):

    if not tasks:
        print("\n❌ No Tasks Found!\n")
        return

    print("\n" + "*" * 70)
    print("                     ALL TASKS")
    print("*" * 70)

    for index, task in enumerate(tasks, start=1):

        print(f"Task No  : {index}")
        print(f"Title    : {task['title']}")
        print(f"Status   : {task['status']}")
        print(f"Priority : {task.get('priority', 'Medium')}")
        print(f"Due Date : {task.get('due_date', 'Not Set')}")
        print("-" * 70)

    print()


# View Pending Tasks
def pending_tasks(tasks):

    print("\n" + "*" * 70)
    print("                  PENDING TASKS")
    print("*" * 70)

    found = False

    for index, task in enumerate(tasks, start=1):

        if task["status"] == "Pending":

            print(f"Task No  : {index}")
            print(f"Title    : {task['title']}")
            print(f"Priority : {task.get('priority', 'Medium')}")
            print(f"Due Date : {task.get('due_date', 'Not Set')}")
            print("-" * 70)

            found = True

    if not found:
        print("🎉 No Pending Tasks!")

    print()


# View Completed Tasks
def completed_tasks(tasks):

    print("\n" + "*" * 70)
    print("                COMPLETED TASKS")
    print("*" * 70)

    found = False

    for index, task in enumerate(tasks, start=1):

        if task["status"] == "Completed":

            print(f"Task No  : {index}")
            print(f"Title    : {task['title']}")
            print(f"Priority : {task.get('priority', 'Medium')}")
            print(f"Due Date : {task.get('due_date', 'Not Set')}")
            print("-" * 70)

            found = True

    if not found:
        print("❌ No Completed Tasks!")

    print()


# Task Statistics
def task_statistics(tasks):

    total = len(tasks)

    pending = 0
    completed = 0

    high = 0
    medium = 0
    low = 0

    for task in tasks:

        if task["status"] == "Pending":
            pending += 1

        elif task["status"] == "Completed":
            completed += 1

        priority = task.get("priority", "Medium")

        if priority == "High":
            high += 1

        elif priority == "Medium":
            medium += 1

        elif priority == "Low":
            low += 1

    print("\n" + "*" * 70)
    print("                 TASK STATISTICS")
    print("*" * 70)

    print(f"📋 Total Tasks      : {total}")
    print(f"⏳ Pending Tasks    : {pending}")
    print(f"✅ Completed Tasks  : {completed}")

    print("-" * 70)

    print(f"🔴 High Priority    : {high}")
    print(f"🟡 Medium Priority  : {medium}")
    print(f"🟢 Low Priority     : {low}")

    print("*" * 70)
    print()