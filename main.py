import json
import sys
import datetime

tasks = []

def check_json():
    pass
def add_task():
     tasks.append({
         "task": input("Enter task name: ")
     })
     with open("Tasks.json",'a') as file:
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

