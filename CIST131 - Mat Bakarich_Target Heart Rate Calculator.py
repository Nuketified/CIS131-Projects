'''Target Heart Rate Calculator'''
# This program gets input from the user and then calculates and outputs the individual's target heart rate.

# maxheart rate = 220 - your age
# target is 50-85% of max


# define main function
def main():
    
    # Initialize variables
    
    # store individual's age
    age = 0
    # store individual's maximum heart rate
    max = 0
    # store value of 50% of max heart rate for later printing
    max50 = 0
    # store value of 85% of max heart rate for later printing
    max85 = 0

    # get and validate input for age
    while True:
            try:
                age = int(input("Please enter the person's age in years. \n"))
                if age < 1:
                    print("Invalid input. Please enter an integer.")
                    continue
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter an integer.")

    # calculate maximum heart rate
    max = 220 - age

    # calculate 50% of maximum heart rate
    max50 = max * .5

    # calculate 85% of maximum heart rate
    max85 = max * .85

    # display the individual's max heart rate and target heart rate to the user.
    print(f"\nThis individual's Maximum Heart Rate is {max} BPM.\n\nThis individual's Target Heart Rate is {max50:.0f}-{max85:.0f} BPM.\n")

# call main function
main()    


