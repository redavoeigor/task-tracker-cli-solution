import json
import datetime

def main():
    #initialise task list
    task_list = []
    choice = 0
    while choice != 6:
        print("*** Task Manager ***")
        print("1) Add the task")
        print("2) Check the task(id, name, group)")
        print("3) Display all tasks")
        print("4) Update the task(status)")
        print("5) Delete the task(id, name, group, 'Are You sure??')")
        print("6) Quit")
        choice = int(input())

if __name__ == "__main__":
    main()
