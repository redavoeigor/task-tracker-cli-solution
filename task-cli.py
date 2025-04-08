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

def main():
    """The main function, that contain all functions for creating, changing, looking, counting and deleting tasks"""
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
            count = 0
            for task in task_list:
                if isinstance(task, dict) and "status" in task and task["status"].lower() == "todo":
                    count += 1
            print(f"\nCount 'todo' : {count}\n")

        elif choice == 5:
            count = 0
            for task in task_list:
                if isinstance(task, dict) and "status" in task and task["status"].lower() == "in-progress":
                    count += 1
            print(f"\nCount 'in-progress' : {count}\n")

        elif choice == 6:
            count = 0
            for task in task_list:
                if isinstance(task, dict) and "status" in task and task["status"].lower() == "done":
                    count += 1
            print(f"\nCount 'done' : {count}\n")

        elif choice == 7:
            print("Updated the task...")
            try:
                task_id = int(input("Please, choose correct id: >>> "))
            except ValueError:
                print("Invalid ID. Please enter a number.")
                continue

            name = input("Change name: >>> ")
            group = input("Change group: >>> ")
            description = input("Change description: >>> ")
            status = input("Change status: >>> ")

            updated = False
            for task in task_list:
                if task["id"] == task_id:
                    if name:
                        task["name"] = name
                    if group:
                        task["group"] = group
                    if description:
                        task["description"] = description
                    if status:
                        task["status"] = status
                        task["updatedAt"] = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
                    updated = True
                    break

            if updated:
                save_tasks(task_list)  # Saving the changes.
                print("Task updated successfully!")
            else:
                print("Task with given ID not found.")

        elif choice == 8:
            print("Delete the task or group")

        elif choice == 9:
            print("Quit")

if __name__ == "__main__":
    main()
