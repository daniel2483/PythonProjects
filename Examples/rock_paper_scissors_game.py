# Rock Paper Scissors

# Exercise 8 (and Solution)

# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

# Remember the rules:
#     Rock beats scissors
#     Scissors beats paper
#     Paper beats rock

def player_info(player):
    name = input(player + " Name:")
    print ('''
    ############ Options ############
    # 1. Rock
    # 2. Paper
    # 3. Scissors
    #################################
    ''')
    correct_option = 0
    while correct_option == 0:
        try:
            selection = int(input("Select a correct option:"))
            if selection == 1 or selection == 2 or selection == 3:
                correct_option = 1
            else:
                correct_option = 0
        except ValueError:
            print("Select a correct option")
            correct_option = 0
    return name,selection

def winner_method(player1,option1,player2,option2):
    winner=player1

    return winner

    
loop = "y"

while loop == "y":
    (player1,option1) = player_info("Player 1")
    (player2,option2) = player_info("Player 2")

    winner_is = winner_method(player1,option2,player2,option2)
    print('''
    
    The winner is''' + winner_is +
    '''
            *           *
        *           *
            *           *
    Congratulations!!!!!!!!!!
    *           *
        *            *
            *           *
    ''')
    loop = input("Do you want to play again (y/n):")
