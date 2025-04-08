import datetime
import utils

def main():
    """The main function, that contain all functions for creating, changing, looking, counting and deleting tasks"""
    task_list = utils.load_tasks()
    while True:
        choice = utils.show_main()
        if choice == 1:
            """Adding the task to task_list.json"""
            print("\nAdding the task...\n")
            if task_list:
                id_task = max(task["id"] for task in task_list) + 1
            else:
                id_task = 1

            name_task = input("Task name: >>> ")
            if len(name_task) > 50:  # Ограничение длины имени задачи
                print("Task name is too long (max 50 characters).")
                return

            group_task = input("Group: >>> ")
            if len(group_task) > 20:  # Ограничение длины группы
                print("Group name is too long (max 20 characters).")
                return

            describe_task = input("Description: >>> ")
            if len(describe_task) > 200:  # Ограничение длины описания
                print("Description is too long (max 200 characters).")
                return

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
            utils.save_tasks(task_list) # Saving the changes.
            print("\nDone successfully!\n")

        elif choice == 2:
            """Searching the task or group"""
            results = []
            query = input("\nSpecify one of the available types of task search: id/name/description/group/status >>> \n")
            for task in task_list:
                if (
                        str(query) == str(task["id"]) or
                        query.lower() in task["name"].lower() or
                        query.lower() in task["description"].lower() or
                        query.lower() in task["group"].lower() or
                        query.lower() in task["status"].lower()
                ):
                    results.append(task)

            if results:
                print("\nYour result:\n")
                for task in results:
                    print('{0} : "{1}" --> {2}'.format(task['id'], task['name'], task['status']))
            else:
                print("\nSorry, we can't find your task :(\nTry >>> 3) 'TASK LIST' for looking all tasks")

        elif choice == 3:
            """Create the tablet of all tasks"""
            if not task_list:
                print("Sorry, the 'TASK LIST' is empty :(\nLet's create new 'TASK LIST' :D")
                utils.load_tasks()
                continue

            while True:
                sub_choice = input("\nEnter sub-command (filter/sort/exit): ")
                if sub_choice.lower() == "filter":
                    utils.filter_tasks(task_list)
                elif sub_choice.lower() == "sort":
                    utils.sort_tasks(task_list)
                elif sub_choice.lower() == "exit":
                    break
                else:
                    print("Invalid sub-command. Try again.")
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
                utils.save_tasks(task_list)  # Saving the changes.
                print("Task updated successfully!")
            else:
                print("Task with given ID not found.")

        elif choice == 8:
            print("Delete the task or group...")
            try:
                delete_choice = int(input("Delete by task ID (1) or group name (2)? >>> "))
                if delete_choice == 1:
                    task_id = int(input("Enter task ID to delete: >>> "))
                    task_list, deleted = utils.delete_task_by_id(task_list, task_id)
                elif delete_choice == 2:
                    group_name = input("Enter group name to delete: >>> ")
                    task_list, deleted = utils.delete_tasks_by_group(task_list, group_name)
                else:
                    print("Invalid choice.")
                    continue
            except ValueError:
                print("Invalid input.")
                continue

            if deleted:
                utils.save_tasks(task_list)
                print("Tasks deleted successfully!")
            else:
                print("Task or group not found.")

        elif choice == 9:
            print("Quit")

if __name__ == "__main__":
    main()
