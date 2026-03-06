import json



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
        if task_name:
            tasks.append({"task": task_name, "progress": "to-do"})
            break
            # save the updated tasks
    with open("Tasks.json",'w') as file:
        json.dump(tasks, file)



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
            json.dump(tasks,file)
    except (IOError,json.JSONDecodeError):
        print("Error in updating task. Please try again.")

def delete_task():
    try: # load the tasks into 'tasks'
        with open("Tasks.json","r") as file:
            tasks = json.load(file)
    except (FileNotFoundError,json.JSONDecodeError):
        print("No tasks available to delete.")
        return
     #display tasks
    print("\nThe tasks found are: ")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task['task']}")

    #  Ask user which task to delete
    try:
        index = int(input("Enter index of task to delete: ")) - 1
        if index < 0 or index >= len(tasks):
            print("Invalid index. Please try again.")
            return
    except ValueError:
        print("Invalid index. Please try again.")
        return
    # Delete the item
    deleted_task = tasks.pop(index)
    try:
        with open("Tasks.json","w") as file:
            json.dump(tasks,file)
            print(f"{deleted_task} deleted successfully!")
    except Exception as e:
        print(f"An error occurred during deleting{e}")

def Mark_Progress():
    try:
        with open("Tasks.json","r") as file:
            tasks = json.load(file)
    except (FileNotFoundError,json.JSONDecodeError):
        print("No tasks available.")
        return

    print("\nThe tasks found are: ")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}.{task['task']} - [{task['progress']}]")

    #ask user which task needs to be updated
    try:
        index = int(input("Enter index of task that needs to update progress: ")) -1
        if index < 0 or index >= len(tasks):
            print("Invalid index. Please try again.")
            return

    except ValueError:
        print("Invalid input. Please enter a number.")
        return


    # Change the progress

    print("\nProgress Choices are: \n1. To-D0\n2. In-Progress\n3. Done ")
    progress_choice = int(input("Enter your choice: "))

    match progress_choice:
        case 1:
            tasks[index]["progress"] = "To-Do"
        case 2:
            tasks[index]["progress"] = "In-Progress"
        case 3:
            tasks[index]["progress"] = "Done"
        case _:
            print("Invalid choice. Please try again.")
            return

    #Save updated tasks
    try:
        with open("Tasks.json","w") as file:
            json.dump(tasks,file)
            print(f"Progress updated to '{tasks[index]['progress']}' successfully!")
    except IOError as e:
        print(f"Error saving progress: {e}")



def list_tasks():

    with open("Tasks.json","r") as file:
         tasks = json.load(file)

    print("Choose which tasks you would like to display: ")
    print("\n1. All Tasks\n2. To-Do\n3. In-Progress\n4. Done")

    try:
        choice = int(input("\nEnter your choice: "))
        todo_tasks = [task for task in tasks if task["progress"] == "To-Do"]
        In_Progress_tasks = [task for task in tasks if task["progress"] == "In-Progress"]
        Done_tasks = [task for task in tasks if task["progress"] == "Done"]

        match choice:
            case 1:
                if not tasks:
                    print("No tasks available to display.")
                else:
                    for index, task in enumerate(tasks, start=1):
                        print(f"{index}. {task['task']} - [{task['progress']}]")


            case 2:
                if not todo_tasks:
                    print("No tasks available to display.")
                else:
                    for index,task in enumerate(todo_tasks, start=1):
                        if task["progress"] == "To-Do":
                            print(f"{index}.{task['task']} - [{task['progress']}]")

            case 3:
                if not In_Progress_tasks:
                    print("No tasks available to display.")
                else:
                    for index,task in enumerate(In_Progress_tasks, start=1):
                        if task["progress"] == "In-Progress":
                            print(f"{index}.{task['task']} - [{task['progress']}]")

            case 4:
                if not Done_tasks:
                    print("No tasks available to display.")
                else:
                    for index,task in enumerate(Done_tasks, start=1):
                        if task["progress"] == "Done":
                            print(f"{index}.{task['task']} - [{task['progress']}]")

            case _:
                print("Invalid choice. Please try again.")
    except ValueError:
        print("Please enter a valid number.")

def task_tracker():

    print("-----Task Tracker-----")
    while True:
        print("\nWhat would you like to do?")
        print("1. Add task", "2. Update task", "3. Delete task", "4. Mark progress", "5. List tasks", "6. Exit\n",
              sep='\n')

        choice = int(input("Enter your choice: "))
        match(choice):
            case 1:
                 print("********************* Add task********************")
                 add_task()
            case 2:
                print("********************* Update task********************")
                update_task()
            case 3:
                print("********************* Delete task********************")
                delete_task()
            case 4:
                print("********************* Mark progress ********************")
                Mark_Progress()
            case 5:
                print("********************* List tasks ********************")
                list_tasks()
            case 6:
                print("See you later!")
                break
            case _:
                 print("Invalid choice. Please try again.")



if __name__ == '__main__':
    task_tracker()

