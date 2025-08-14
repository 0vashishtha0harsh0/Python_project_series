import os
import json
from datetime import datetime

Task_file = "Task.json"

def load_task():
   try:
       with open(Task_file, "r") as f:
           return json.load(f)
   except FileNotFoundError:
       return[]

def save_tasks(Task):
    with open(Task_file, "w") as f:
        return json.dump(Task, f, indent=4)

def view_tasks(Task):
    if not Task:
        print("No task Present to view...")
        return
    print("Your Tasks.........")
    for idx, Task_item in enumerate(Task,1):
        if isinstance(Task_item,str):
            Title = Task_item
            Priority = "Medium"
            Deadline = "N/A"
        else:
            Title = Task_item.get("Title") or Task_item.get("title") or "<notitle>"
            Priority = Task_item.get("Priority") or Task_item.get("priority") or "Medium"
            Deadline = Task_item.get("Deadline") or Task_item.get("deadline") or "N/A"
            
            print(f"{idx}.{Title} | priority : {Priority} | deadline: {Deadline}")        
    

def show_menu():
    print("To do tasks -----")
    print("1.Add tasks")
    print("2.Remove tasks")
    print("3.View tasks")
    print("4.Exit....")

Task = load_task()

while True:
    show_menu()
    choice = int(input("choose an option "))

    if(choice == 1):
        Title = input("Enter task Title : ").strip()
        Priority= input("Enter the Priority of task(High/Medium/Low) : ").strip()
        Deadline = input("Enter the Deadline (YYYY-MM-DD) : ").strip()
        

        try:
            datetime.strptime(Deadline, "%Y-%m-%d")
            Task.append({"Title": Title, "Priority":Priority.capitalize(), "Deadline":Deadline})
            save_tasks(Task)

            print("Task is Added successfully............")

        except ValueError:
            print("Enter the date in 'YYYY-MM-DD' format")
    elif(choice == 2):
        if not Task:
            print("No task present to remove *")

        else:
            try:
                task_no = int(input("Enter the Task number which you want to remove....... : "))
                if(task_no >= 1 and task_no <= len(Task)):
                    remove = Task.pop(task_no-1)
                    save_tasks(Task)
                    if isinstance(remove, str):
                        print(f"Task {remove} removed successfully......")
                    else:
                        print(f"Task {remove.get('Title') or remove.get('title')}")
                    

                else:
                    print("Task Number dont't exists")

            except ValueError:
                print("Please enter the valid number ")

    elif(choice == 3):
        view_tasks(Task)
        
    elif(choice == 4):
        print("Goodbye.....")

        break
    else :
        print("Print the choice from the above menu")
        
        
    
    
