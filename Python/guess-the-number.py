# guess the number between 1-20

# The program will first randomly generate a number unknown to the user. The user needs to guess what that number is. If the user’s guess is wrong, the program should return some sort of indication as to how wrong. If the user guesses correctly, a positive indication should appear.

import random

ranNum = random.randint(1, 10)
tries = 0 

def compare(g, ranNum):
    if g > 10:
        print('This number is not between 1 & 10')
    else:
        if g > ranNum:
            print('\nYour answer is too high')
        if g < ranNum:
            print('\nYour answer is too low')

print(ranNum)
while (tries < 5):
    g = int(input('\nPlease guess number between 1-10: '))
    if g != ranNum:
        compare(g, ranNum)
        tries = tries + 1
        print('')
        triesLeft = str(tries) + '/5 tries left..'
        print(triesLeft)
    else:
        print('\nYou got it correct!')
        break
 
if tries == 5:
        print('\nYou have run out of tries')
