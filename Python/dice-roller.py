#   When the program runs, it will randomly choose a number between 1 and 6.
#   It should then ask you if you’d like to roll again.

import random
roll = input('Roll Dice?: ') # Ask user if they want to roll some dice
if roll == 'no':
        print('\nWhy did you even run this?') # if they say no, ask why they ran it in the first place

while (roll == 'yes'):  # if yes then print a number 1-6
    print("")
    print(random.randint(1, 6)) 
    roll = input('\nWould you like to roll again?: ') #if they would like to roll again prevents infinite while-loop
    if roll == 'no': # if they no longer want to play end the game.
        print('\nThanks for playing!')
