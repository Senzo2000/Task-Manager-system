import datetime

def reg_user():
    new_username = input("Enter new username : \n")
    while new_username in username:
        print("error!! enter a new username.\n")
        new_username = input("Enter new username : \n")


    newpassword = input("Enter a new password: ")
    confirm_password = input("\nconfrim your password: ")
    
    while newpassword != confirm_password:
         print("Password do not match")
         confirm_password = input("Please Re-enter you password")

    with open('user.txt','a') as u:
        u.write("\n"+new_username + ", " + newpassword)

def add_task():
    username = input("Enter your username: ")
    title = input("Enter the title of your task: ")
    description = input("Description of task: ")
    due_date = input("Enter the due date of your task: ")
    date = datetime.date.today()
    task_completed = 'No'
   
    with open('output1.txt','a') as tasks:
       # for line in tasks :
            tasks.write("\n" + username + ", " + title + ", " + description + ", " + str(
            date) + ", " + due_date + ", " + task_completed)

def view_all():
    #if options == "va":
        with open('output1.txt', 'r') as tasks:
            for line in tasks:
                line = line.split(", ")
                #Taking info [indexes] from the file and showcasing it with the programme
                print("Task:" "\t" + line[1])
                print("Assigned to:" "\t" + line[0])
                print("Date assigned:" "\t" + line[3])
                print("Due date:"  "\t" + line[4])
                print("Task complete?:" "\t" + line[5])
                print("Task description:" "\t" +line[2])
                print("=====================\n")
                
            tasks.close()
            

def view_my():
   # if options == "vm":
        with open('output1.txt', 'r') as f:
            for lineNumber,line in f:
                line = line.split(", ")
              
            print("Task Number: " + str(lineNumber))
            print("Task:\t" + line[1])
            print("Assigned to:\t" + line[0])
            print("Date assigned:\t" + line[3])
            print("Due date:\t" + line[4])
            print("Task complete:\t" + line[5].strip('\n'))
            print("Task description:\n" + line[2])
            print("\n")
            #filename.seek(0)

            # asking user to select the task number they will like to change
            tnum = int(input("Please select Task Number you would like to change: "))

            for lineNumber, line in enumerate(line): 
                # for lineNumber, line in enumerate(lines)
                # task_list is initialize to line.split(', ") that is putting comma and space in task_list
                line = line.split(", ")
                # if name is equal to task_list[0] that index [0]
                if tnum == lineNumber:
                    option2 = int(input("Would you like to change:\n"
                                        "1. - edit task\n"
                                        "2. - mark complete\n"
                                       "-1. - return to main menu\n"))
                
                if (option2 != 1) or (option2!= 2) or (option2!=- 1):
                        print("invalid number try again:")
                
                if option2 == 1:
                        
                        if line[5].strip('\n') == 'No':
                            edit = input('''What would you like to edit:
                                            u - username\n
                                            d - due date\n''')
                            if edit == "u":
                                # updating a field
                                line = line.split(", ")
                                newUserName = input("Please input new user: ")
                                line = line.replace(line[0], newUserName)
                                print(line)  
                                line[lineNumber - 1] = line
                                print(line)
                                data_to_file = '\n'.join(line)
                                print(data_to_file)
                                new_task_file = open('tasks.txt', 'w+')
                                new_task_file.write(data_to_file)

                            if edit == "d":
                                # updating details
                                line= line.split(", ")
                                due_date = input("Please input new due date: ")
                                line = line.replace(line[4], due_date)
                                print(line)
                                line[lineNumber - 1] = line
                                print(line)
                                data_to_file = '\n'.join(line)
                                print(data_to_file)
                                new_task_file = open('tasks.txt', 'w+')
                                new_task_file.write(data_to_file)

                elif option2 == 2:
                        
                        if line[5].strip('\n') == 'No':
                            task_complete = input('enter yes or no: ')

                            if task_complete == "Yes" or "No":
                                # updating a field
                                line = line.split(", ")
                                yes = input("enter yes or no: ")
                                line = line.replace(line[-1], yes)
                               
                                print(line)
                                line[lineNumber - 1] = line
                                print(line)
                                data_to_file = '\n'.join(line)
                                print(data_to_file)
                                new_task_file = open('output1', 'w+')
                                new_task_file.write(data_to_file)
                                print('successfully updated the file')
def task_overview():
    if options == 'gr':

        with open('task_overview.txt', 'r', encoding='utf-8') as task:
            print('\nOver view of tasks:\n')
            print("===================\n")
            for line in task:
                print(line.strip())

        task_count = 0
        task_complete = 0
        incompleted_tasks = 0
        tasks_overdue = 0

        # open and read the content of tasks.txt as task
        with open('tasks.txt', 'r+', encoding='utf-8') as task:

            for line in task: 

                line = line.split(", ")  
                datetime_object = datetime.datetime.strptime(line[4], '%Y-%m-%d')
                task_count += 1 

            if line[-1].strip("\n") == 'Yes':
                   task_complete += 1  

            # elif task_list at index position -1 strip new line character is equal to 'No'
            elif line[-1].strip("\n") == 'No':
                incompleted_tasks += 1  # uncompleted_task is set to plus(+) equal 1

            # if datetime_object is less than datetime.datetime.today and task_list at index position 5 strip new
            # line character is equal to 'No'
            if datetime_object < datetime.datetime.today() and line[5].strip("\n") == 'No':
                tasks_overdue += 1  
                print(f"The number of tasks is: {task_count}")
                print(f"The number of complete tasks is: {task_complete}")
                print(f"The number of incomplete tasks is: {incompleted_tasks}")
                print(f"The number of overdue tasks is: {tasks_overdue}")

            #  performing the calculation of the content
            percentage_incomplete = (incompleted_tasks * 100) / task_count
            percentage_overdue = (tasks_overdue * 100) / task_count

            # Print / write everything to the file.
            task = open('tasks_overview.txt', 'w', encoding='utf-8')
            task.write(f"\nTotal number of tasks generated using Task Manager: {task_count}\n")
            task.write(f"Number of completed tasks: {task_complete}\n")
            task.write(f"Number of uncompleted tasks: {incompleted_tasks}\n")
            task.write(f"Number of uncompleted tasks that are overdue: {tasks_overdue:.0f}\n")
            task.write(f"Percentage of uncompleted tasks: {percentage_incomplete:.0f}%\n")
            task.write(f"Percentage of uncompleted overdue tasks: {percentage_overdue:.0f}%\n\n")
                         
            
    
with open('user.txt','r') as f:
        for line in f:
            f.readline().strip("\n")
            print(line)
            fusername = line.split(', ')
            fpassword = line.split(', ')

        username = input("Enter a valid username: ")
        password = input("Enter a valid password: ")

        while (username != "admin") or (password != "adm1n"):
            username = input("Incorrect username, Enter a valid username: ")
            password = input("Incorrect password, Enter a valid password: ")

#After login
        if (username == "admin") and (password == "adm1n"):
            options = input("Please select one of the following options:" "\n"
                "r  -  register users" "\n"
                "a  - add task" "\n"
                "va - view all tasks" "\n"
                "vm - view my tasks" "\n"
                "e  - exit" "\n"
                "ds - display statistics" "\n"
                "ta - task overview" "\n")
    
#the users input will be sent to the function , on the top and it will do what it is required
#calling of functions 
if options == "r":
    reg_user()

if options == "a":
    add_task()

if options == "va":
    view_all()

if options == "vm":
    view_my()
     
if options =="ta":
    task_overview()  
