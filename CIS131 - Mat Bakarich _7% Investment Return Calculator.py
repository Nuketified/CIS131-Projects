'''7% Investment Return Calculator'''

# This program will calculate the return on the principal investment over a set time.

# define main function
def calc():
    # Initialize constants.
    # Interest rate as a decimal
    INTEREST_RATE = .07
    # specified times periods to accrue interest
    PERIOD_1 = 10
    PERIOD_2 = 20
    PERIOD_3 = 30


    # Initialize variables. 
    principal = 0
    total = 0
    years = 0
    # store totals to print later
    ten_years = 0
    twenty_years = 0
    thirty_years = 0
    
    # Get and validate user input for principal amount
    while True:
        try:
            principal = int(input("Please enter the principal amount in dollars. \n"))
            if principal < 1:
                print("Invalid input. Please enter ana positive integer.")
                continue
            else:
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")


    # Get and validate user input for number of years to accrue interest
    while True:
        try:
            years = int(input("Please enter the number of years to accrue interest. \n"))
            if years < 1:
                print("Invalid input. Please enter a positive integer.\n")
                continue
            else:
                break
        except ValueError:
            print("Invalid input. Please enter an integer.\n")


    # formula to calculate total with interest for values inputted by user
    total = principal * (1 + INTEREST_RATE)**years
    
    # calculate total with interest for specified values of 10, 20, and 30 year periods.
    ten_years = principal * (1+ INTEREST_RATE)**PERIOD_1
    twenty_years = principal * (1+ INTEREST_RATE)**PERIOD_2
    thirty_years = principal * (1+ INTEREST_RATE)**PERIOD_3

    # print the totals to the user.
    print(f"\nThe total with interest after {years} years is ${total:.2f}.\n\nThe total after 10 years will be ${ten_years:.2f}.\nThe total after 20 years will be ${twenty_years:.2f}.\nThe total after 30 years will be ${thirty_years:.2f}.\n")

# call to main function
calc()
    