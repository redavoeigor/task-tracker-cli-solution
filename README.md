# Task Manager CLI
url: https://roadmap.sh/projects/task-tracker

## Description

This command line tool (CLI) allows you to manage your task list. You can add, search, display, count, update and delete tasks. The data is stored in the `task_list.json` file.

## Requirements

- Python 3.x
- Python standard libraries (datetime, json, os)

## Installation

1. Copy the `task-cli.py` and `utils.py` files to the same directory.

2. Make sure you have Python 3.x installed.

## Usage

Run the `task-cli.py` script from the command line:

```bash
python task-cli.py
```
After launching, you will be offered a menu with available commands:
```
*** Task Manager ***

1) Add new task
2) Search and sort
3) Display all tasks
4) Count 'todo'
5) Count 'in-progress'
6) Count 'done'
7) Update the task
8) Delete the task or group
9) Quit
```
## Commands

1. Add new task:
* Requests the name, group, and description of the task.
* Adds the task to the list.
* Limitations: task name (30 characters), group (20 characters), description (50 characters).

2. Search and sort:
* Requests the search criteria (id, name, description, group, status).
* Displays the search results.

3. Display all tasks:
* Displays all tasks in a table.
* Allows you to filter and sort tasks within the table.
- filter: Filters tasks by id, name, group, status, date.
- sort: Sorts tasks by id, name, group, status, date.
- exit: Exit subcommands.

4. Count 'todo':
* Counts the number of tasks with the "todo" status.

5. Count 'in-progress':
* Counts the number of tasks with the "in-progress" status.

6. Count 'done':
* Counts the number of tasks with the "done" status.

7. Update the task:
* Requests the task ID to update.
* Allows you to change the name, group, description, and status of the task.
* Updates updatedAt when the status changes.

8. Delete the task or group:
* Allows you to delete a task by ID or a group of tasks by group name.

9. Quit:
* Exit the program.

## Structure of the task_list.json file
The task_list.json file stores tasks in the following format:

# JSON
```
{
"TaskList": [
{
"id": 1,
"name": "Write a report",
"group": "Work",
"description": "Prepare a monthly report",
"status": "todo",
"createdAt": "10/20/2023 10:00",
"updatedAt": null
},
{
"id": 2,
"name": "Call a client",
"group": "Work",
"description": "Specify project details",
"status": "in-progress",
"createdAt": "10/20/2023 11:00",
"updatedAt": "10/20/2023 12:00"
} ]
}
```
## Notes

If the task_list.json file does not exist, it will be created automatically.
When working with dates, the format is "DD/MM/YYYY HH:MM".
The input length limits help maintain the readability of the table.
Author
redavoeigor

License
This `README.txt` provides a complete description of your project, including installation and usage instructions. You can add or modify sections to suit your needs.
