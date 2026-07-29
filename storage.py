import json
import os

# JSON File Name
FILE_NAME = "tasks.json"

# Load Tasks
def load_tasks():

    # Agar file exist nahi karti
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r") as file:
            tasks = json.load(file)

            # Old tasks ke liye default values add karo
            for task in tasks:
                task.setdefault("priority", "Medium")
                task.setdefault("due_date", "Not Set")

            return tasks

    except (json.JSONDecodeError, FileNotFoundError):
        return []

# Save Tasks
def save_tasks(tasks):

    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)