import json
import sys
import datetime
from asyncio import tasks
from unittest import case


def add_task():
    try:
        # First read the file to see if anything already exists
        with open("Tasks.json", 'r') as file:
            tasks = json.load(file)
    except (FileNotFoundError,json.JSONDecodeError):
        tasks = []
        #add tasks taken from the user
    while True:
        task_name = input("Enter task name: (or type q to quit):  ").strip()

        if task_name.lower() == "q":
            break
        if task_name.isalpha():
            tasks.append({"task": task_name})

            # save the updated tasks
    with open("Tasks.json",'w') as file:
        file.write(json.dumps(tasks))


def update_task():
    #  Load tasks safely
    try:
      with open("Tasks.json","r") as file:
          tasks = json.load(file)
    except (FileNotFoundError,json.JSONDecodeError):
        print("No tasks found! Please add one.")
        return

    # Display tasks with numbers
    print("\nThe tasks found are: ")
    for index,task in enumerate(tasks, start=1):
        print(f"{index}. {task['task']}")

    #  Ask user which task to update
    try:
         index = int(input("Enter index of task to update: ")) - 1
         if index < 0 or index >= len(tasks):
             print("Invalid index. Please try again.")
             return
    except ValueError:
        print("Invalid index. Please try again.")
        return

    # Ask for new task name

    new_task = input("Enter new task (or q to exit): ").strip()
    if new_task.lower() == "q":
        return
# Step 5: Update the task in memory
    try:
        old_task = tasks[index]["task"]
        tasks[index]["task"] = new_task

# Step 6: Write the updated tasks back to the file

        with open("Tasks.json", 'w') as file:
            json.dumps(tasks,file)
    except (IOError,json.JSONDecodeError):
        print("Error in updating task. Please try again.")

def delete_task():
    pass
def Mark_Progress(name):
    pass
    # in-progress, done
def list_tasks():
    #all, done, not-done, in-progress
    pass
def task_tracker():

    print("-----Task Tracker-----")
    print("What would you like to do?")
    print("1. Add task","2. Update task","3. Delete task","4. Mark progress","5. List tasks","6. Exit\n", sep='\n')


    while True:
        choice = int(input("Enter your choice: "))
        match(choice):
            case 1:
                 add_task()
            case 2:
                 update_task()
            case 3:
                 delete_task()
            case 4:
                 Mark_Progress()
            case 5:
                 list_tasks()
            case 6:
                print("See you later!")
                break
            case _:
                 print("Invalid choice. Please try again.")



if __name__ == '__main__':
    task_tracker()

