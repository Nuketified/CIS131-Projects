"""The Miles Per Gallon Calculator"""
# This program will take inputs from the user, then display MPG calculations

# define the main function
def mpg():
        
    # define variables
    gallons = 0
    miles = 0
    mpg = 0
    gallons_total = 0
    miles_total = 0
    mpg_total = 0

    # define variables for loop
    keep_going = 0
    
    # main program loop to take inputs
    while keep_going != -1:
        
        # get and validate gallons input
        while True:
            # get the gallons input from the user 
            try:
                gallons = float(input("Enter the gallons used (-1 to end.):"))       
                # validate the input
                if gallons == -1:
                     break
                elif gallons <= 0 and gallons != -1:
                    print("Value must be greater than 0.")    
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")
            

    
 
        # break from loop here when sentinel is entered
        keep_going = gallons
        if keep_going == -1:
                break
        # when sentinel is not entered, continue and get and validate miles input
        else:    
            while True:
                # get the miles input from the user
                try:
                    miles = float(input("Enter the miles driven:"))
                    # validate the input
                
                    if miles <= 0:
                        print("Value must be greater than 0.")
                    else:
                        break
                except ValueError:
                    print("Invalid input. please enter a number.")
            
            # calculate miles per gallon and assign to 'mpg'
            mpg = miles/gallons
            # track total gallons
            gallons_total+=gallons
            # track total miles
            miles_total+=miles
            # print the mpg for the current entries
            print(f"The miles/gallon for this tank was {mpg:.2f}")

    
    # calculate the overall miles per gallon
    mpg_total = miles_total/gallons_total

    
    # print the overall miles per gallon
    print(f"The overall average miles/gallon was {mpg_total:.2f}") 

# call main function
mpg()    