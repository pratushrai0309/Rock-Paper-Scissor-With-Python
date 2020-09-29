
#Rock Paper Scissor With Python
#Author => Pratush Rai
#Github Repository => https://github.com/pratushrai0309/Rock-Paper-Scissor-With-Python/blob/master/rockpaperscissor.py
#Follow Me On Twitter => https://twitter.com/PratushRai
#Follow Me On Github => https://github.com/pratushrai0309

import random

#Used Variables
computer_Choice = ''

computer_Score = 0
player_Score = 0

print('Welcome to python Rock Paper Scissor OO || ><')
print('Type help for more information')

name = input('Please Enter The Player Name: ')

for i in range(1, 15):

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
        >quit to quit the game[y -- yes , n -- no]
        ''')

    if player_Choice == 'quit':
        ans = input('Do you really want to quit [y / n]: ')

        if ans == 'y':
            break

        else:
            continue

    #Game Winning Logic
    if player_Choice == computer_Choice:
        print('The match is tie')
        computer_Score += 1
        player_Score += 1
        print('Computer Score => ',computer_Score, name,'Score => ', player_Score)

    if player_Choice == 'Rock' and computer_Choice == 'Paper':
        print('Computer Wins :(')
        computer_Score += 1
        print('Computer Score => ',computer_Score, name,'Score => ', player_Score)

    elif player_Choice == 'Paper' and computer_Choice == 'Rock':
        print(name,' Win :)')
        player_Score += 1
        print('Computer Score => ',computer_Score, name,'Score => ', player_Score)

    elif player_Choice == 'Paper' and computer_Choice == 'Scissor':
        print('Computer Wins :(')
        computer_Score += 1
        print('Computer Score => ',computer_Score, name,'Score => ', player_Score)

    if player_Choice == 'Scissor' and computer_Choice == 'Paper':
        print(name,' Win :)')
        player_Score += 1
        print('Computer Score => ',computer_Score, name,'Score => ', player_Score)

    if player_Choice == 'Scissor' and computer_Choice == 'Rock':
        print('Computer Wins :(')
        computer_Score += 1
        print('Computer Score => ',computer_Score, name,'Score => ', player_Score)

    elif player_Choice == 'Rock' and computer_Choice == 'Scissor':
        print(name,' Win :)')
        player_Score += 1
        print('Computer Score => ',computer_Score, name,'Score => ', player_Score)
    
    #Game Score Logic
    if computer_Score == 5:
        print('The Final Winner Is Computer []--===')
        break

    elif player_Score == 5:
        print('The Final Winner Is ',name,' [] --===')
        break

else:
    print('The Game is complete')
