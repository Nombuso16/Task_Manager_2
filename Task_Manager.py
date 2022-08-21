#==================importing============================================
import datetime
from datetime import *
    

# Creating functions to register the user
def reg_user(menu_choice):
    #testin if the r option was selected
    if menu_choice == "r":  
        
        #asking for the user to to enter a new user name
        username_new = input("Please enter a new username: \n  ")

        # Checking if the username already exists in the usernames_list.
        # Whilst listed, the user is prompted to re-enter a new username and an error message is displayed.
        while username_new in usernames_list:

            #pritning an error if the new user name entered already exxists
            print("Ooops! Username already exists.\n *")

            uername_new = input("Please enter a new username: \n *")
   
        # If the new username is not already listed, it is added to usernames_list.
        if username_new not in usernames_list:

            usernames_list.append(username_new)

            user_details["Usernames"] = usernames_list  # The updated list is then updated in the dictionary user_details.
          
        # allow user to enter the password      
        new_password_entry = input("Enter a new password: \n *")

        # The user is asked to confirm their new password entered.
        pass_confirm_entry = input("Confirm your new password: \n *")        

        # If the new password and confirmed password values do not match
        while new_password_entry != pass_confirm_entry:
            
            #error message is displayed.
            print("\nYour passwords do not match - Attempt again.\n *")
            #ask the user for password inputs again
            new_password = input("Please enter your new password: \n - *")
            pass_confirm = input("Please confirm your new password: \n - *") 
            
        # If the new and confirmed password match
        if new_password_entry == pass_confirm_entry:
            
            # The new password is added to the passwords_list.
            passwords_list.append(new_password_entry)  

            # The updated list is updated in the dictionary user_details.
            user_details["Passwords"] = passwords_list  

            # opening user text file
            with open('user.txt', 'r+') as info:

                # Using for statement to print username and passwords on separate lines.
                # The number of lines is equal to the number of items in usernames_list.
                for i in range(len(usernames_list)):

                        # Writing from the apppropriate dictionary keys, in the correct format. 
                        info.write(user_details["Usernames"][i] + ", " + user_details["Passwords"][i] + '\n')
                        
        
        return("\n Succesfully added, Thank you!!!")


# Creating a function to add a new task
def add_task(menu_choice):

    if menu_choice == "a":

        import datetime
        from datetime import date

        # asking the user user for the task that is assigned to.
        name = input("May you enter the username of the individual you are to assign the task to: \n * ")
        
        # Getting user input on the title of the task being added. 
        title = input("May you enter the title of the task: \n * ")
        
        # asking for the description of the added task.
        descrip = input("May you enter a description of the task: \n * ")

        # calculating the current date.
        current_date = datetime.date.today()

        # locking the date into a date format
        assigned_date = current_date.strftime('%d %b %Y')

        # asking the user to entr the due date of the task being added.
        date_format = input("May you enter the due date of the task (e.g. dd-mm-yyyy): \n * ")

        dates = date_format.split("/")

        numbers_date = [int(i) for i in dates]

        due_date = date(numbers_date[2], numbers_date[1], numbers_date[0]).strftime('%d %b %Y') 

        # automatically setting task_completed to "No" when adding new task. 
        task_completed = "No"

        # Casting all user input info into a list, to add to the tasks_dict.
        task_list = [name, title, descrip, assigned_date, due_date, task_completed]

        tasks_dict[f"Task {count} details:"] = task_list    

        # Opening the tasks.txt file and entering the new task info.
        with open('tasks.txt', 'r+') as information:

            # Printing the list values for each key in tasks_dict to a new line.
            for key in tasks_dict:

                # Converting the info into a string enabling the info to be written to the file.
                string = str(tasks_dict[key])  

                bad_characters = ["[", "]", "\'",]  

                # Taking out characters pertaining to previous list/dictionary format.
                for a in bad_characters:  

                    string = string.replace(a, "")

                # Writing the correct format of each string line to the task file
                information.write(string + '\n')  

        # displaying message  
        return("\nYour new task has been added successfully.")

# CreatingfFunction to view all tasks 
# These tasks are already stored in the dictionary 'tasks_dict'.
# Therefore, the dictionary will be used to view all the tasks.
def view_all(menu_choice):

    if menu_choice == "va":

        count = 0

        for key in tasks_dict:

            task_count += 1

            print(f"""

Task {str(count)}:          {str(tasks_dict[key][1])}
Assigned to:                {str(tasks_dict[key][0])}
Date assigned:              {str(tasks_dict[key][3])}
Due Date:                   {str(tasks_dict[key][4])}
Task Complete?              {str(tasks_dict[key][5])}
Task Description:
{str(tasks_dict[key][2])}""")

    return("The End!!!")

# Creating function to view all tasks assigned to the logged in user.
def view_mine(menu_choice, username):

    if menu_choice == "vm":

        # Setting a count for number of tasks.
        task_count = 0  

        for key in tasks_dict:

            # calculating the total number of tasks by appending the count through tasks_dict
            task_count += 1  

            # testing if the task is assigned to the user and displaying it
            if username == (tasks_dict[key][0]):  

                print(f"""

Task {str(task_count)}:       {str(tasks_dict[key][1])}
Assigned to:            {str(tasks_dict[key][0])}
Date assigned:          {str(tasks_dict[key][3])}
Due Date:               {str(tasks_dict[key][4])}
Task Complete?          {str(tasks_dict[key][5])}
Task Description:
{str(tasks_dict[key][2])}""")  


    # enabling the user to choose to either edit a task by number or return to the main menu.
    task_select = int(input("""\n May you select task number to edit or type 99 to return to the main menu. \n : """))

    task_select = task_select - 1
    
    with open('tasks.txt', 'r') as file:
        task_file = file.readlines()
        
    for line in task_file:
            print(f'\n{task_file[task_select]}')
            break
        
    # If they select '99', they return to the main menu.
    if task_select == "99":  

        return(menu)        
    
    # If they enter a task number, they can choose to mark as complete or edit.        
    else:  

       option = input("""\nWould you like to label the task as complete or Edit the task: 
                        L - Label
                        E - Edit  
                        : """).casefold()
       
       if option == "L":
           
           x = (task_file[task_select])
           # Finding the position
           user_task = task_file[task_select].strip().split(",")

           new_state = task_file[task_select].strip().replace(user_task[5], ' Yes')

           task_file.pop(task_select)

           task_file.append(new_state)

           print(f'\n{new_state}\n')
           
           # Deleting the old file    
           list = []
           with open(r"tasks.txt", 'r') as file_position:
                list = fp.readlines()
           with open(r"tasks.txt", 'w') as file_position:
                for number, text in enumerate(list):
                    if number not in [task_select]:
                        file_position.write(text)
                        
           # Updating tasks file and appending new updated task
           with open('tasks.txt', 'a') as file:
                file.write(f'\n{new_state}')

           return("\nLabelled as task completed!!!")
                
       # If they choose to edit, the task must be incomplete, when the specific item in dictionary list equal to 'No'.
       elif option == "E": 

           #option to edit username or due date.
           edit_choice = input("""\nDo you want to edit the task username or due date: 
                                                    U - Username
                                                    D - Due Date  
                                                    : """).casefold()

           # If they choose to edit the username, they must enter a new username for the task.
           if edit_choice == "u":  
               
               x = (task_file[task_select])
               # Finding the position
               user_task = task_file[task_select].strip().split(",")

               new_state = task_file[task_select].strip().replace(user_task[0], input("Change username \n * "))

               task_file.pop(task_select)

               task_file.append(new_state)

               print(f'\n{new_state}\n')
           
               # Delete the old task    
               list = []
               with open(r"tasks.txt", 'r') as file_position:

                   l1 = fp.readlines()

               with open(r"tasks.txt", 'w') as file_position:

                   for number, line in enumerate(l1):

                       if number not in [task_select]:

                           fp.write(line)
                        
               # Updating tasks file and appending new updated task
               with open('tasks.txt', 'a') as file:
                   file.write(f'\n{new_state}')

               return("\nUsername updated successfully!!!")  
          
           # If they choose to edit the due date, they are prompted to enter a new date. 
           elif edit_choice == "d":  
               
               x = (task_file[task_select])
               # Finding the position
               user_task = task_file[task_select].strip().split(",")

               new_state = task_file[task_select].strip().replace(user_task[4], input("Enter a new due date (e.g. 17 July 2021) \n * "))

               task_file.pop(task_select)

               task_file.append(new_state)

               print(f'\n{new_state}\n')
           
               # Deleting the old task    
               list = []
               with open(r"tasks.txt", 'r') as fp:

                   l1 = fp.readlines()

               with open(r"tasks.txt", 'w') as fp:

                   for number, line in enumerate(l1):

                       if number not in [task_select]:

                           fp.write(line)
                        
               # Updating tasks file and appending new updated task
               with open('tasks.txt', 'a') as file:
                   file.write(f'\n{new_state}')

               return("Due date successfully updated")  
           

''' 
Function to check over due
check whether a task is overdue by comparing due date and current date
if the current date is greater than the due date, then the task is over due. 
 '''
def over_due_check(due_date):

    # Setting Boolean false for the task as over_due.  
    over_due = False  

    # ===================import========================
    import datetime
    from datetime import date

    ''' The dates in this task are in the format '17 Jul 2022' as a string.
     this needs to be converted to integers to compare dates.
     1. the variable is split into a list.
     '''
    list_dates = due_date.split()
    # The first item is converted into an integer and stored in the 'day' variable.
    day = int(list_dates[0])
     # The second item is converted into an integer and stored in the 'year' variable.  
    year = int(list_dates[2]) 

    # A month dictionary with number values is setted to enable calculation of string month into an integer. 
    months_dict = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul':7, 'Aug': 8, 'Sep':  9, 'Oct': 10, 'Nov': 11, 'Dec': 12}

    ''' The corresponding value of the key in months_dict which is equal to list_dates[1] (i.e. 'jan', 'Jul' etc.) is stored in 'month'.
    # This will be a number value from the appropriate key in months_dict.'''
    month = months_dict[list_dates[1][0:3]]

    # finding the current date using the datetime module and formatting it into the same format at the due date initially was.
    date_now = datetime.date.today().strftime('%d %b %Y')

    # The same process is repeated for the current date. Firstly, it is split into a list of items.
    date_now_list = date_now.split()

    # The first item is stored as an integer in day_2.
    day2 = int(date_now_list[0])
    # Second item is stored as an integer in year_2.  
    year2 = int(date_now_list[2])  
    # The corresponding integer value from months_dict at appropriate key is stored in month_2.
    month2 = months_dict[date_now_list[1]]  

    ''' Now that we have integers for year, day and month to work with, two dates can be created in the correct format for comparison.
    # date_1 is the due date and date_2 is the current date.'''
    date1 = date(year, month, day)
    date2 = date(year2, month2, day2)

    # If current date is greater than set due date, over_due_date is changed to 'True'
    if date2 > date1:  

        # over_due date is returned
        over_due_date = True
        return(over_due_date)  

    # If set due date is greater than current date, over_due_date is 'False'
    elif date1 > date2 or date1 == date2:  

        # over_due value is returned.
        over_due_date = False
        return(over_due_date)  

# Creating function to Generate text files 'task_overview.txt' and 'user_overview.txt'
def generate_reports():

    # Setting blank strings to store info in to be written to the generated text files
    task_overview = ""  
    user_overview = ""

    tasks_total = len(tasks_dict)  # Total number of tasks is equal to the key count of tasks_dict
        
    # Adding a string with the total tasks number to the tas_overview string. 
    task_overview = task_overview + f"The total number of tasks generated and tracked by task_manager.py is {str(len(tasks_dict))}."

    # Setting variables for integers concerning complete tasks, incomplete tasks and overdue tasks respectively.
    first = 0  
    second = 0
    third = 0
        
    for key in tasks_dict:

        # Checking for which tasks are complete by finding the 'Yes' string in each key of tasks_dict
        if tasks_dict[key][5] == "Yes": 

            # If the task is complete, string item is present, variable x is increased by 1.
            first += 1       

        # Checking for which tasks are complete by finding the 'No' string in each key of tasks_dict
        elif tasks_dict[key][5] == "No":  
            
            # If the task is complete, i.e. 'No' string item is present, variable y is increased by 1
           second += 1  

           if over_due_check(tasks_dict[key][4]):  # If the over_due_check function returns 'True', a task is overdue and incomplete.

               third += 1  # 'z' is increased by 1 to count the incomplete, overdue tasks.   

    ''' 
    All of the numbers calculated above are now built into sentences in the task_overview string.
    Percentages are also calculated within the f-strings added, with the results being rounded to 2 decimal places and cast into strings into sentences
    '''
    task_overview = task_overview + f"\nThe total number of completed tasks is {str(first)}." + f"\nThe total number of incomplete tasks is {str(second)}."
    task_overview = task_overview + f"\nThe total number of incomplete and overdue tasks is {str(third)}."
    task_overview = task_overview + f"\nThe percentage of incomplete tasks is {str(round((second / len(tasks_dict)) * 100, 2))}%."
    task_overview = task_overview + f"\nThe percentage of tasks that are overdue {str(round((third / len(tasks_dict)) * 100, 2))}%."

    # Now generating a 'task_overview' file and the task_overview string is then written to the file in an easy to read format.
    with open('task_overview.txt', 'w') as files:

        files.write(task_overview)
    '''
    Setting variables to store information regarding total users, complete tasks for a user, incomplete tasks for the user,
    incomplete and over-due tasks for the user respectively.
    '''
    a = 0
    b = 0
    c = 0
    d = 0

    for key in tasks_dict:

        if tasks_dict[key][0] == username:  # Counting the number of tasks assigned to the user by identifying the first list item.

            a += 1  # Integer 'a' is increased by 1 if the task is for the user.

        elif tasks_dict[key][0] == username and tasks_dict[key][5] == "Yes":  # Checking if the task for the user is complete.

           b += 1  # Integer 'b' is increased by 1 if the task is complete.     

        elif tasks_dict[key][0] == username and tasks_dict[key][5] == "No":  # Checking if the task for the user is incomplete.

            c += 1  # Integer 'c' is increased by 1 if the task is incomplete.  

            if over_due_check(tasks_dict[key][4]):  # Checking if the task is incomplete and overdue.

                d += 1  # If overdue, integer 'd' is increased by 1.
         
    # Writing all the info calculated above into sentence strings which are built into the user_overview string variable.
    user_overview = user_overview + f"The total number of users registered with task_manager.py is {str(len(user_details))}."
    user_overview = user_overview + f"\nThe total number of tasks generated and tracked by task_manager.py is {str(len(tasks_dict))}."
    user_overview = user_overview + f"\nThe total number of tasks assigned to {username} is {str(a)}."
    user_overview = user_overview + f"\nThe percentage of the total number of tasks assigned to {username} is {str(round((a / len(tasks_dict)) * 100, 2))}%."
    user_overview = user_overview + f"\nThe percentage of tasks assigned to {username} that have been completed is {str(round((b / a) * 100, 2))}%."
    user_overview = user_overview + f"\nThe percentage of tasks still to be completed by {username} is {str(round((c / a) * 100, 2))}%."
    user_overview = user_overview + f"\nThe percentage of incomplete and overdue tasks assigned to {username} is {str(round((d / a) * 100, 2))}%."

    # Now generating a 'user_overview' file.
    # The user_overview string is then written to the file in an easy to read format.
    with open('user_overview.txt', 'w') as f4:

        f4.write(user_overview)        

    # The user then views a message stating that their reports have been successfully generated.
    # They do not have the option to view the reports.
    # The admin user can select to display statistics from their main menu.
    return("\nYour reports have been generated successfully.")

    
# Writing the program.    
# Firstly, I will build the current info from tasks.txt and user.txt into appropriate lists and dictionaries.
# This will allow me to build and work with the information in an easier way. 
# In the first version of this code, I used a string to store the user and task contents.
# Now, the user and tasks details will be stored in corresponding dictionaries for use in the program.
user_details = {}

# The user details dictionary will be built with lists from 'usernames_list' and 'passwords_list' as values.
usernames_list = []
passwords_list = []

tasks_dict = {}

# Opening the tasks.txt file to read and write information from it.
# Adding the info in the user.txt file into the set list.
with open('user.txt', 'r+') as f:

    for line in f:

        newline = line.rstrip('\n')  # Stripping newline characters from the line.
        
        split_line = newline.split(", ")  # Splitting the line into a list.
        
        usernames_list.append(split_line[0])  # Assigning items from the list into corresponding list.
        passwords_list.append(split_line[1])

        user_details["Usernames"] = usernames_list  # Lists are now stored as values assigned to keys in user_details dictionary.
        user_details["Passwords"] = passwords_list      


# Setting a count to keep track of the number of lines in the tasks.txt file.
count = 1

# Opening the tasks.txt file to read and write information to it.
with open('tasks.txt', 'r+') as f2:

    for line in f2:
        
        newline = line.rstrip('\n')  # Stripping newline characters.
        
        split_line = newline.split(", ")  # Splitting line into a list of items.

        tasks_dict[f"Task {count} details:"] = split_line # Assigning each list of items to a key in tasks_dict.

        count += 1  # Count used to change key value for each list of info.

# Task Manager login code.
# Getting input from the user on their login details.
print("\nWelcome to your Task Manager!\n")

username = input("Enter your username: \n - ")
password = input("\nEnter your password: \n - ")

# Creating a while loop to run whilst login details are incorrect.
while (username not in usernames_list) or (password not in passwords_list):

        # If username is correct and password is correct, the following message is displayed.
        if (username not in usernames_list) and (password in passwords_list):

            print("\nusername is not registered - try again\n")

            username = input("Re-enter your username: \n - ")   
            password = input("Re-enter your password: \n - ")

        # If password is incorrect and username is correct, the following message is displayed.
        elif (password not in passwords_list) and (username in usernames_list):

            print("\nYour password is incorrect - Please try again.\n")

            username = input("Please re-enter your username: \n - ")
            password = input("Please re-enter your password: \n - ")

        # If both the username and password are incorrect, the following message is displayed. 
        elif (username not in usernames_list) and (password not in passwords_list):

            print("\nYour username and password are incorrect.\n")

            username = input("Please re-enter your username: \n - ")
            password = input("Please re-enter your password: \n - ")

# If both username and password are correct, the successful login message is displayed.            
if (username in usernames_list) and (password in passwords_list):

    print("\nLogin Successful...")


# While loop to display the menu once the user is logged in. 
while 1:

    # The admin user menu.
    if username == "admin":  

        menu = input("""\nPlease select one of the following options:

                r  - Register user
                a  - Add task
                va - View all tasks
                vm - View my tasks
                gr - Generate reports
                ds - Display statistics
                e  - Exit
                : """).casefold()            

    else:  # All other users menu. 

       menu = input("""\nMay you select one of the following options:

                a  - Add task
                va - View all tasks
                vm - View my tasks
                gr - Generate reports
                e  - Exit
                : """).casefold()
    
    # 'r' = register new user function
    if menu == "r":  

        print(reg_user(menu))

    # 'a' = add new task function
    elif menu == "a": 

        print(add_task(menu))

    # va' = view all task function
    elif menu == "va":   

        print(view_all(menu))

    # 'vm' view my tasks function 
    elif menu == "vm":  

       print(view_mine(menu, username))

    # 'gr' = generate reports fuction
    elif menu == "gr":  

        # Calling function to generate report files.
        print(generate_reports())  
        
    elif menu == 'ds':

        # Calling function generate files in case they do no exist yet.
        print(generate_reports())  

        # Heading printed for user-friendly display.
        print("\nThe task overview report is as follows:\n")  

        # Opening the task_overview file to get info from it
        with open('task_overview.txt', 'r+') as f3:  

            for line in f3:

                print(line)  # Printing/displaying each line in the file.

        # Heading printed for user_friendly display.
        print("\nThe user overview report is as follows:\n") 

        # Opening user_overview file.
        with open('user_overview.txt', 'r+') as f4:  

            for line in f4:

                # Displaying each line of the file.
                print(line)  

        # Ending the reports display.
        print("\nEnd of Statistics Reports\n")  

    elif menu == "e":  

        print("\nSuccessfully logged out.\n")
        break   
        

                    

                

                

           

                    
                

        

    




           





        

    

    




    





    

        

        

        


            

            
            

                    

                    

                

                

                

            



            






                       







