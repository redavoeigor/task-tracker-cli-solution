import json
import datetime

def load_tasks(filepath="task_list.json"):
    """Download tasks from JSON."""
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
    taskList = load_tasks()
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
            # По-потел над первым функционалом...
            print("\nAdding the task...\n")
            if taskList:
                id_task = max(task["id"] for task in taskList) + 1
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
            taskList.append(task)
            with open("task_list.json", "w", encoding="utf-8") as outfile:
                json.dump({"TaskList": taskList}, outfile, indent=4, ensure_ascii=False)
            print("\nDone successfully!\n")

        elif choice == 2:
            results = []
            query = input("\nSpecify one of the available types of task search: id/name/description/group >>> \n")
            for task in taskList:
                if str(query) == str(task["id"]) or query.lower() in task["name"].lower() or query.lower() in task["description"].lower() or query.lower() in task["group"].lower():
                    results.append(task)
                    print('\nYour result:\n\n{0} : "{1}" --> {2}\n'.format(task['id'], task['name'], task['status']))
            if results == []:
                print("\nSorry, we can't find your task :(\nTry >>> 3) 'TASK LIST' for looking all tasks")

        elif choice == 3:
            print("'TASK LIST'\n___________")

        elif choice == 4:
            print("Updating the task...")

        elif choice == 5:
            print("Remove the task...")

        elif choice == 6:
            print("Closing...\n__________")

        elif choice == 7:
            print("Updating the task...")

        elif choice == 8:
            print("Remove the task...")

        elif choice == 9:
            print("Closing...\n__________")

if __name__ == "__main__":
    main()
