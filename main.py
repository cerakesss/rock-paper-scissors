import random

def who_win(userhod, bothod):
    if userhod == bothod:
        print(f'Tie! Bot threw {bothod}')
    # if you threw rock the program checks: if you threw rock and bot threw scissors you win, if you threw rock and bot threw paper you lose, and so on below
    elif (
        (userhod == 'Rock' and bothod == 'Scissors') or
        (userhod == 'Scissors' and bothod == 'Paper') or
        (userhod == 'Paper' and bothod == 'Rock')
    ):
        print(f'You won! Bot chose {bothod}')
    else:
        print(f'You lost! Bot chose {bothod}')

def bot_hod_gen(botrand):
    # if bot chose 1 then it threw rock
    if botrand == 1:
        rps2 = 'Rock'
    # if bot chose 2 then it threw scissors
    elif botrand == 2:
        rps2 = "Scissors"
    # if none of the above happened then bot threw paper
    else:
        rps2 = 'Paper'
    return rps2


# game loop
while True:
    # generate what the bot will throw
    rps = random.randint(1, 3)
    
    # what the user will throw
    rps3 = input('Choose what you want to pick, rock, scissors, paper: ').capitalize()

    commands_list = ['quit', 'q','exit']
    if rps3 in commands_list:
        print('Shutting down!')
        break

    elif rps3 not in ['Rock', 'Scissors', 'Paper']:
        print('Error! Enter one of the allowed values.')
        continue

    rps2 = bot_hod_gen(rps)

    who_win(rps3, rps2)
