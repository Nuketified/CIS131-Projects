"""Guess the Number Game"""
# this program will allow the user to play a number guessing-game

# import random
import random

# define the main function
def game():
    # define constants
    NUMBER_CAP = 1000
    # change this constant to change the guess range to 1 to NUMBER_CAP 
    TARGET_GUESSES = 10
    # change this constant to change the target number of guesses for "knowing the secret"

    # define variables
    
    # store random integer
    number = 0
    # store player guess
    guess = 0
    # count number of guesses
    guesses = 0

    # variable to keep playing
    keep_going = "yes"

    # main guessing game loop
    while keep_going == "yes":
        # get a random integer
        number = random.randint(1, NUMBER_CAP)
        # set number of guesses to 0.
        guesses = 0
        # set guess to blank
        guess = 0
        # loop to take and check guesses
        while guess != number:
            while True:    
                try:
                    guess= int(input(f"Guess my number between 1 and {NUMBER_CAP} with the fewest guesses:"))
                except ValueError:
                    print(f"Please enter an integer from 1-{NUMBER_CAP}.")
                if guess > NUMBER_CAP or guess < 1:
                    print(f"Please enter an integer from 1-{NUMBER_CAP}.")
                else:
                    break    
         
            # print feedback for guess too high
            if guess > number:
                print("Too high, try again.")
            # print feedback for guess too low
            if guess < number:
                print("Too low, try again.")
            # add one to "number of guesses" counter
            guesses+=1
            # break out of loop when the correct number is guessed
            if guess == number:
                break
        
        # tell user they guessed the correct number
        print("Congratulations. You guessed the number!") 
        
        # display number of guesses
        print(f"\nNumber of guesses:{guesses}.\n")
        
        # print text to user based on how many guesses were used
        if guesses <=TARGET_GUESSES:
            print("Either you know the secret or you got lucky!\n")
        if guesses > TARGET_GUESSES:
            print("You should be able to do better!\n")
    
           
        # get user input to keep playing or end the game
        keep_going = input("Would you like to play again?\n")
                
        # convert to lower case
        keep_going = keep_going.lower()
        
        
        # accept "y" or "yes" to continue playing
        if keep_going == "y" or keep_going == "yes":
            keep_going = "yes"

        # print when user chooses not to keep playing    
        else: print("Thanks for playing. See you next time!")





# call the main function
game()    