#To-Do List Project

#   Create two empty list vars
#   Create 4 custom funcs
#   add_tasks()
#   rmv_tasks()
#   completed_tasks()
#   display_list()
#
#   Display a menu for the user
#   in a while loop:
#       Use error handling to prompt the user for an approproate input:
#           If the user gives an unacceptable input, throw them an error
#           If users iput an appropriate answer, follow through with the interactive menu.
#           When users are done with the program, allow them to exit the program.

task_list = []
task_stat = []

def add_tasks():
    user_add = input("What task do you wish to add to the list? ").capitalize()
    task_list.append(user_add)
    task_stat.append(False) # <--- This will make the task have an automatic imcomplete status

def rmv_tasks():
    user_dlt = input("What task do you wish to delete from the list? ").capitalize()
    task_list.remove(user_dlt)
    
def completed_tasks():
    user_task_fin = input("What task did you finish? ").capitalize()
    if user_task_fin in task_list:
        task_fin = task_list.index(user_task_fin)
        task_stat[task_fin] = True 
    else:
        print(f"{user_task_fin} is not in the list of tasks.")

def display_list():
    if len(task_list) == 0:
        print("The list is empty")
    else:
        for i in range(len(task_list)):
            stat = "Completed" if task_stat[i] else "Incomplete"
            print(f"Task: {task_list[i]} -- {stat}")

while True:
    print("\tMenu\n1. Add a Task\n2. Remove a Tasks\n3. Mark a Task as Complete\n4. Diplay List\n5. Quit\n What would you like to do?")
    try:
        user_choice = int(input("Select a number from the menu: "))
    except ValueError:
        print("Please enter a number between 1 - 5.")
    else:
        match user_choice: 
            case 1:      
                add_tasks()
                pass
            case 2:
                rmv_tasks()
                pass
            case 3:
                completed_tasks()  
                pass                 
            case 4:
                display_list()
                pass
            case 5:
                print("Thank you for using Task Management Pro. Have a great rest of your day!")
                break