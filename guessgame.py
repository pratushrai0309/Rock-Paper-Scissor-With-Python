import random

secretNum = random.randint(1, 100)

print(secretNum)

for i in range(1, 10):
    guessNum = int(input('Guess a number: '))

    if guessNum < secretNum:
        print('You guessed number lower than the secret number')
    
    elif guessNum > secretNum:
        print('You guessed number larger than the secret number')

    if guessNum == secretNum:
        print('You won')
        break
else:
    print('Your chance are over')