started = False
print('Welcome to my stoopid game! ')
help_input = input('Type \"help\" for help or \"quit\" to quit the game \n>').casefold()
while help_input != 'quit':

    if help_input == "help":
        option = input('start - to start car\nstop - to stop car\nquit - to quit\n>').casefold()

        while option != "quit":
            if option == "start":
                if started == False:
                    option = input('You have started the car\n>').casefold()
                    started = True
                else:
                    option = input('Car already started bro!\n>').casefold()

            elif option == "stop":
                if started == True:
                    option = input('You have stopped the car\n>').casefold()
                    started = False
                else:
                    option = input('Car already stopped bro!\n>').casefold()


            else:
                option = input('Invalid! Enter the following options:\nstart - to start car\nstop - to stop car\nquit - to quit\n>')
        break
    else:
        help_input = input('Type \"help\" for help or \"quit\" to quit the game \n>')

print("Goodbye")









