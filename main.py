import json
import sys
import datetime

 # the add functions creates a list everytime the script runs so need to read the json file and read it to see if it's empty

def add_task():
    try:
        # First read the file to see if anything already exists
        with open("Tasks.json", 'r') as file:
            tasks = json.load(file)
    except (FileNotFoundError,json.JSONDecodeError):
        tasks = []
        #add tasks taken from the user
    while True:
        task_name = input("Enter task name: (or type q to quit):  ")

        if task_name == "q":
            break
        tasks.append({"task": task_name})

            # save the updated tasks
        with open("Tasks.json",'w') as file:
             file.write(json.dumps(tasks))



def update_task():
    pass
def delete_task():
    pass
def Mark_Progress(name):
    pass
    # in-progress, done
def list_tasks():
    #all, done, not-done, in-progress
    pass
def task_tracker():
    add_task()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    task_tracker()

