import random


# game loop
while True:
    # generate bot's choice
    rps = random.randint(1, 3)
    
    # get user's choice
    rps3 = input('Choose what you want to pick, rock, scissors or paper: ')

    # if bot chose 1 then it's rock
    if rps == 1:
        rps2 = 'Rock'
    # if bot chose 2 then it's scissors
    elif rps == 2:
        rps2 = "Scissors"
    # if none of the above happened then bot chose paper
    else:
        rps2 = 'Paper'

    # if your choice and bot's choice are the same then it's a tie
    if rps3 == rps2:
        print(f'Tie! Bot threw {rps2}')
    # if you threw rock the program checks: if you threw rock and bot threw scissors you win, if you threw rock and bot threw paper you lose, and so on below
    elif (
        (rps3 == 'Rock' and rps2 == 'Scissors') or
        (rps3 == 'Scissors' and rps2 == 'Paper') or
        (rps3 == 'Paper' and rps2 == 'Rock')
    ):
        print(f'You won! Bot chose {rps2}')
    else:
        print(f'You lost! Bot chose {rps2}')
