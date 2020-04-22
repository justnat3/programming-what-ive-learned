#The Goal: Remember Adventure? Well, we’re going to build a more basic version of that. A complete text game, the program will let users move through rooms based on user input and get descriptions of each room. To create this, you’ll need to establish the directions in which the user can move, a way to track how far the user has moved (and therefore which room he/she is in), and to print out a description. You’ll also need to set limits for how far the user can move. In other words, create “walls” around the rooms that tell the user, “You can’t move further in this direction.”


# Concepts to keep in mind:

# Strings
# Variables
# Input/Output
# If/Else Statements
# Print
# List
# Integers

# How do you want to accomplish this?
# player has to move
#   define rooms and a description of those rooms
#   let user just naviagte from room to room keep it simple
#   track how far they have moved
#   which room am I in? can I reach the description of the room?
#   have 4 rooms

# player doesn't have to own anything just rooms for now.


#rows
# x = a, b
# y = a, d

# (x,y)  (0,0) (0,1) 


#index 
# testScores = [93,23,54,74,60,80]

#colums


room = [
              ['a', 'b',],
              ['d', 'e',],
          ]

# moveLeft = 'left'
# moveRight = 'right'
# moveUp = 'up'
# moveDown = 'down'

# rooms
room1 = room[0][0]
room2 = room[0][1]
room3 = room[1][1]
room4 = room[1][0]

#  room descriptions

room1des = '\nCold stone walls surround you, Its dark.. there is a door obscured by the darkness on your right along with your way back down' #top left
room2des = '\nThe room is filled with light by the torch on a piller in the middle of the room.. There is a door, left and up. ' #top right
room3des = '\nthe room is that of a bar with no one in it. You are alone there is a door going back and to your left leading to room1' # bottom right
room4des = '\nthis room is pitch black, there is nothing of interest that you can see at least there is a door to your right and door ahead of you(up)' # bottom left

options = print('Your Options to move:' + '\nCurrentRoom' + '\nLeft' + '\nDown' + '\nRight' + '\nUp')

mv = input('\nchoose from your options')

startRoom = print(room2)

