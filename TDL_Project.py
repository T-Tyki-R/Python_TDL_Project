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
    pass

def rmv_tasks():
    pass

def completed_tasks():
    pass

def display_list():
    pass

while True:
    print("\tMenu\n1. Add a Task\n2. Remove a Tasks\n3. Mark a Task as Complete\n4. Diplay List\n5. Quit\n What would you like to do?")
    try:
        user_choice = int(input("Select a number from the menu: "))
    except ValueError:
        print("Please enter a number between 1 - 5.")
    else:
        match user_choice: 
            case 1:      
                # add_tasks()
                pass
            case 2:
                #rmv_tasks()
                pass
            case 3:
                # completed_tasks()  
                pass                 
            case 4:
                #display_list()
                pass
            case 5:
                print("Thank you for using Task Management Pro. Have a great rest of your day!")
                break