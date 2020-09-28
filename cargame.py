
command = ''
started = False

while command != 'quit':

    command = input('>')

    if command == 'help':
           print('''Start --> To start the cars
 Stop --> To stop the car
Quit --> To quit the game''')
          
    elif command == 'Start':
        if started == False:
            print('The car is started. Ready to go o||o')
            started = True
        else:
            print('The car is already started')

    elif command == 'Stop':
        if not started == True:
            print('The car is already stopped')
            started = True
        else:
            print('Car stopped')

    elif command == 'quit':
        print('Quitting out of the game :)')

    else:
        print('Wrong command type help for all the supported commands')

