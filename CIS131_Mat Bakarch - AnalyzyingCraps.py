"""Analyzing the Game of Craps"""
# this


def main():

    # define constant for number of games to play
    GAMES_TO_PLAY = 1000000

    # initaalize dictionaries to store wins and losses
    wins = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0, 21: 0, 22: 0, 23: 0, 24: 0, 25: 0,}
    losses = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0, 21: 0, 22: 0, 23: 0, 24: 0, 25: 0,}
    wins_and_losses = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0, 21: 0, 22: 0, 
    23: 0, 24: 0, 25: 0, 26: 0, 27: 0, 28: 0, 29: 0, 30: 0, 31: 0, 32: 0, 33: 0, 34: 0, 35: 0, 36: 0, 37: 0, 38: 0, 39: 0, 40: 0, 41: 0, 42: 0, 43: 0, 44: 0, 45: 0, 
    46: 0, 47: 0, 48: 0, 49: 0, 50: 0}
    
    # initialize variables for storing % of games resolved
    percent_on_roll = 0
    total_percent = 0
    # counter for while loop
    games_played = 0
    # number of die rolls
    die_rolls = 0

    # intialize variables for calculating and storing win and loss percentages
    games_won = 0
    games_lost = 0
    win_percent = 0
    lose_percent = 0





    # fig04_02.py
    """Simulating the dice game Craps."""
    import random

    def roll_dice():
        """Roll two dice and return their face values as a tuple."""
        die1 = random.randrange(1, 7)
        die2 = random.randrange(1, 7)
        return (die1, die2)  # pack die face values into a tuple



    def display_dice(dice):
        """Display one roll of the two dice."""
        die1, die2 = dice  # unpack the tuple into variables die1 and die2
    #    print(f'Player rolled {die1} + {die2} = {sum(dice)}')




    while games_played < GAMES_TO_PLAY:
        
        # set/rest die_rolls to 0 
        die_rolls = 0

        # inital die roll
        die_values = roll_dice()  # first roll
       
        # increment die rolls counter
        die_rolls+=1
    

        # determine game status and point, based on first roll
        sum_of_dice = sum(die_values)

        if sum_of_dice in (7, 11):  # win
            game_status = 'WON'
            # increment games won counter
            games_won+=1
            # record win to win dictionary
            if game_status =='WON' and die_rolls in wins:
                wins[die_rolls]+=1
            else:
                wins[die_rolls]=1
        elif sum_of_dice in (2, 3, 12):  # lose
            game_status = 'LOST'
            # increment games lost counter
            games_lost+=1
            # record loss to losses dictionary
            if game_status == 'LOST' and die_rolls in losses:    
                losses[die_rolls]+=1
            else:
                losses[die_rolls]=1

        else:  # remember point
            game_status = 'CONTINUE'
            my_point = sum_of_dice
      

        # continue rolling until player wins or loses
        while game_status == 'CONTINUE':
            die_values = roll_dice()
            display_dice(die_values)
            sum_of_dice = sum(die_values)
            die_rolls+=1

            if sum_of_dice == my_point:  # win by making point
                game_status = 'WON'
                # increment counter for number of games won
                games_won+=1
                # record win to win dictionary
                if game_status =='WON' and die_rolls in wins:
                    wins[die_rolls]+=1
                else:
                    wins[die_rolls]=1 
                    
            elif sum_of_dice == 7:  # lose by rolling 7
                game_status = 'LOST'
                # increment counter for number of games lost
                games_lost+=1
                # record loss to losses dictionary
                if game_status == 'LOST' and die_rolls in losses:    
                    losses[die_rolls]+=1
                else:
                    losses[die_rolls]=1
        
        # record total wins and losses for each number of rolls 
        if game_status != 'CONTINUE' and die_rolls in wins_and_losses:
            wins_and_losses[die_rolls]+=1
        else:
            wins_and_losses[die_rolls]=1            

        
        # increment games played counter
        games_played+=1

    
    # calculate percentage of games won 
    win_percent = 100 * games_won/games_played
    # calculate percentage of games lost
    lose_percent = 100 * games_lost/games_played

    # print win and loss perecentages
    print(f"\nPercentage of wins: {win_percent:.2f}%\n\nPercentage of losses: {lose_percent:.2f}%\n"  )
    # print first line of table output
    print("# of    % Resolved     Cumulative %\nRolls   on this roll   of games resolved\n")
    # iterate over wins and losses dictionary to print output table
    for key, value in wins_and_losses.items():
        # calculate and store % of games resolved by this roll
        percent_on_roll = 100 * value/games_played
        # add that value to the cumulative % of games resolved by this roll
        total_percent+=percent_on_roll 
        # print the table
        print(f"{key:02d}      {percent_on_roll:.2f}          {total_percent:.2f}" )
    
    # print contents of Wins dict for confirmation
    print("\nWins:",wins,"\n")
    # print contents of Losses dict for confirmation
    print("Losses:",losses,"\n")
    
    
    
# call main function
main()