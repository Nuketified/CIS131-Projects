"""Input Grades to Text."""
# This program takes and validates user input before writing valid grades to a text file.
def input_grades():
    
    # initialize variables
    user_input =""
    
    try:
        # open or create file for writing
        with open('grades.txt', mode='w') as grades:
            # loop to get and validate user input
            while user_input != "-1":         
                user_input=input("Please enter a grade, -1 to quit.")
                if user_input.isdigit() == False and user_input != "-1" and user_input != "":
                   print("Please enter only positive intgers or -1") 
                if user_input == "":
                    print("No grade entered.") 
                if  user_input != "-1" and user_input != "" and user_input.isdigit() == True: 
                    print(user_input, file=grades)
    # handle permission errors.
    except PermissionError:
        print("Permission Error. Please check filepath and permissions and try again.")
    # prints confirmation that the program has ended.
    print("Program ended.")


input_grades()
