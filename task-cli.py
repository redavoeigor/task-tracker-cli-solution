import json
import datetime

def load_tasks(filepath="task_list.json"):
    """Download task_list from JSON."""
    try:
        with open("task_list.json", "r", encoding="utf-8") as infile:
            data = json.load(infile)
            if isinstance(data, dict) and "TaskList" in data and isinstance(data["TaskList"], list):
                return data["TaskList"]  # Возвращаем список задач
            else:
                print(f"File {"task_list.json"} contains invalid data.")
                return []
    except FileNotFoundError:
        print(f"File {"task_list.json"} not found.")
        return []
    except json.JSONDecodeError:
        print(f"File {"task_list.json"} contains invalid JSON.")
        return []


def main():
    """The main function, that contain all functions for creating, changing, looking and deleting tasks"""
    task_list = load_tasks()
    choice = 0
    while choice != 9:
        print("\n*** Task Manager ***\n")
        print("1) Add the task(name, and description, and group; {auto todo})")
        print("2) Update the status(id, or name; {todo}/{in-progress}/{done})")
        print("3) Display all tasks(or group)(task:{id}, {description}, {group}, {status}, {createdAt}, {updatedAt})")
        print("4) Count 'todo'(sum all status {todo})")
        print("5) Count 'in-progress'(sum all status {in-progress})")
        print("6) Count 'done'(sum all status {done})")
        print("7) Update the task(name, description)")
        print("8) Delete the task or group(id, or name, or group; 'Are You sure??')")
        print("9) Quit\n")
        choice = int(input())

        if choice == 1:
            """Adding the task to task_list.json"""
            print("\nAdding the task...\n")
            if task_list:
                id_task = max(task["id"] for task in task_list) + 1
            else:
                id_task = 1
            name_task = str(input("Task name: >>> "))
            group_task = str(input("Group: >>> "))
            describe_task = str(input("Description: >>> "))
            status_task = "todo"
            created_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
            task = {
                "id": id_task,
                "name": name_task,
                "group": group_task,
                "description": describe_task,
                "status": status_task,
                "createdAt": created_date,
                "updatedAt": None
            }
            task_list.append(task)
            with open("task_list.json", "w", encoding="utf-8") as outfile:
                json.dump({"TaskList": task_list}, outfile, indent=4, ensure_ascii=False)
            print("\nDone successfully!\n")

        elif choice == 2:
            """Searching the task or group"""
            results = []
            query = input("\nSpecify one of the available types of task search: id/name/description/group >>> \n")
            for task in task_list:
                if str(query) == str(task["id"]) or query.lower() in task["name"].lower() or query.lower() in task["description"].lower() or query.lower() in task["group"].lower():
                    results.append(task)
                    print('\nYour result:\n\n{0} : "{1}" --> {2}\n'.format(task['id'], task['name'], task['status']))
            if not results:
                print("\nSorry, we can't find your task :(\nTry >>> 3) 'TASK LIST' for looking all tasks")

        elif choice == 3:
            """Create the tablet of all tasks"""
            if not task_list:
                print("Sorry, the 'TASK LIST' is empty :(\nLet's create new 'TASK LIST' :D")
                return load_tasks()
            id_width = 4
            group_width = 10
            name_width = 20
            status_width = 12
            print("___TASK LIST___".center(50) + "\n" + "-" * (id_width + group_width + name_width + status_width + 13))
            print(f"| {'ID'.ljust(id_width)} | {'Group'.ljust(group_width)} | {'Name'.ljust(name_width)} | {'Status'.ljust(status_width)} |")
            print("-" * (id_width + group_width + name_width + status_width + 13))  # Разделитель

            for task in task_list:
                print(f"| {str(task['id']).ljust(id_width)} | {str(task['group']).ljust(group_width)} | {task['name'].ljust(name_width)} | {task['status'].ljust(status_width)} |")

        elif choice == 4:
            print("Count 'todo'")

        elif choice == 5:
            print("Count 'in-progress'")

        elif choice == 6:
            print("Count 'done'")

        elif choice == 7:
            print("Update the task")

        elif choice == 8:
            print("Delete the task or group")

        elif choice == 9:
            print("Quit")

if __name__ == "__main__":
    main()
