
#Rock Paper Scissor With Python
#Author => Pratush Rai
#Github Repository => 

import random

computer_Choice = ''

print('Welcome to python Rock Paper Scissor OO || ><')
print('Type help for more information')

for i in range(1, 11):

    #Computer Choice
    computer_Number = random.randint(1, 3)
    if computer_Number == 1:
        computer_Choice = 'Rock'

    elif computer_Number == 2:
        computer_Choice = 'Paper'

    elif computer_Number == 3:
        computer_Choice = 'Scissor'

    #Player Choice
    player_Choice = input('> ')

    if player_Choice == 'Rock':
        print('You choose Rock...OO==--')

    elif player_Choice == 'Paper':
        print('You choose Paper...||==--')

    elif player_Choice == 'Scissor':
        print('You choose Scissor...><==--')

    if player_Choice == 'help':
        print('''
        >Paper for paper
        >Scissir for scissor
        >Rock for rock
        >quit to quit the game
        ''')

    if player_Choice == 'quit':
        ans = input('Do you really want to quit [y / n]: ')
        if ans == 'y':
            break
        else:
            continue

    if player_Choice == computer_Choice:
        print('The match is tie')

    if player_Choice == 'Rock' and computer_Choice == 'Paper':
        print('Computer Wins :(')

    elif player_Choice == 'Paper' and computer_Choice == 'Rock':
        print('You Win :)')

    elif player_Choice == 'Paper' and computer_Choice == 'Scissor':
        print('Computer Wins :(')

    if player_Choice == 'Scissor' and computer_Choice == 'Paper':
        print('You Win :)')

    if player_Choice == 'Scissor' and computer_Choice == 'Rock':
        print('Computer Wins :(')

    elif player_Choice == 'Rock' and computer_Choice == 'Scissor':
        print('You Win :)')

else:
    print('The Game is complete')
