import json
import datetime

def load_tasks(filepath="task_list.json"):
    """Download task_list from JSON."""
    try:
        with open("task_list.json", "r", encoding="utf-8") as infile:
            data = json.load(infile)
            if isinstance(data, dict) and "TaskList" in data and isinstance(data["TaskList"], list):
                return data["TaskList"]  # Returning a list of tasks
            else:
                print(f"File {"task_list.json"} contains invalid data.")
                return []
    except FileNotFoundError:
        print(f"File {"task_list.json"} not found.")
        return []
    except json.JSONDecodeError:
        print(f"File {"task_list.json"} contains invalid JSON.")
        return []

def save_tasks(tasks, filepath="task_list.json"):
    """Saving tasks in JSON file."""
    with open(filepath, "w", encoding="utf-8") as outfile:
        json.dump({"TaskList": tasks}, outfile, indent=4, ensure_ascii=False)

def delete_task_by_id(task_list, task_id):
    """Deletes a task by ID."""
    deleted = False
    updated_task_list = []
    for task in task_list:
        if task["id"] == task_id:
            deleted = True
        else:
            updated_task_list.append(task)
    return updated_task_list, deleted

def delete_tasks_by_group(task_list, group_name):
    """Deletes tasks by group name."""
    deleted = False
    updated_task_list = []
    for task in task_list:
        if task["group"] == group_name:
            deleted = True
        else:
            updated_task_list.append(task)
    return updated_task_list, deleted

def show_main():
    """Shows the main menu and returns the user's selection."""
    print("\n*** Task Manager ***\n")
    print("1) Add the task")
    print("2) Searching tasks")
    print("3) Display all tasks")
    print("4) Count 'todo'")
    print("5) Count 'in-progress'")
    print("6) Count 'done'")
    print("7) Update the task")
    print("8) Delete the task or group")
    print("9) Quit\n")

    while True:
        try:
            choice = int(input("Your choice (1-9): >>> "))
            if 1 <= choice <= 9:
                return choice
            else:
                print("Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def filter_tasks(tasks):
    """Filters tasks based on user input."""
    print("\nFilter by: id/name/group/status/date")
    filter_by = input("Enter filter criteria: ").lower()

    if filter_by == "id":
        try:
            filter_id = int(input("Enter task ID: "))
            filtered = [task for task in tasks if task["id"] == filter_id]
        except ValueError:
            print("Invalid ID format.")
            return
    elif filter_by == "name":
        filter_name = input("Enter task name: ").lower()
        filtered = [task for task in tasks if filter_name in task["name"].lower()]
    elif filter_by == "group":
        filter_group = input("Enter group name: ").lower()
        filtered = [task for task in tasks if filter_group in task["group"].lower()]
    elif filter_by == "status":
        filter_status = input("Enter task status: ").lower()
        filtered = [task for task in tasks if filter_status == task["status"].lower()]
    elif filter_by == "date":
        start_date = input("Enter start date (DD/MM/YYYY HH:MM): ")
        end_date = input("Enter end date (DD/MM/YYYY HH:MM): ")
        try:
            start_datetime = datetime.datetime.strptime(start_date, "%d/%m/%Y %H:%M")
            end_datetime = datetime.datetime.strptime(end_date, "%d/%m/%Y %H:%M")
            filtered = [
                task
                for task in tasks
                if start_datetime <= datetime.datetime.strptime(task["createdAt"], "%d/%m/%Y %H:%M") <= end_datetime
            ]
        except ValueError:
            print("Invalid date format. Please use DD/MM/YYYY HH:MM")
            return
    else:
        print("Invalid filter criteria.")
        return

    if filtered:
        # Вывод отфильтрованных задач в виде таблицы
        print_tasks_table(filtered)
    else:
        print("No tasks found matching the filter criteria.")

def sort_tasks(tasks):
    """Sorts tasks based on user input."""
    print("\nSort by: id/name/group/status/date")
    sort_by = input("Enter sort criteria: ").lower()

    if sort_by == "id":
        sorted_tasks = sorted(tasks, key=lambda task: task["id"])
    elif sort_by == "name":
        sorted_tasks = sorted(tasks, key=lambda task: task["name"].lower())
    elif sort_by == "group":
        sorted_tasks = sorted(tasks, key=lambda task: task["group"].lower())
    elif sort_by == "status":
        sorted_tasks = sorted(tasks, key=lambda task: task["status"].lower())
    elif sort_by == "date":
        sorted_tasks = sorted(tasks, key=lambda task: datetime.datetime.strptime(task["createdAt"], "%d/%m/%Y %H:%M"))
    else:
        print("Invalid sort criteria.")
        return

    # Вывод отсортированных задач в виде таблицы
    print_tasks_table(sorted_tasks)

def print_tasks_table(tasks):
    """Prints tasks in a formatted table."""
    id_width = max(len(str(task['id'])) for task in tasks) + 2
    group_width = max(len(task['group']) for task in tasks) + 2
    name_width = max(len(task['name']) for task in tasks) + 2
    status_width = max(len(task['status']) for task in tasks) + 2

    print("___TASK LIST___".center(sum([id_width, group_width, name_width, status_width, 7])))
    print("-" * sum([id_width, group_width, name_width, status_width, 7]))
    print(f"| {'ID'.ljust(id_width)} | {'Group'.ljust(group_width)} | {'Name'.ljust(name_width)} | {'Status'.ljust(status_width)} |")
    print("-" * sum([id_width, group_width, name_width, status_width, 7]))

    for task in tasks:
        print(f"| {str(task['id']).ljust(id_width)} | {task['group'].ljust(group_width)} | {task['name'].ljust(name_width)} | {task['status'].ljust(status_width)} |")

