# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random

#global variable secret_number declared
secret_number = 0
#global variable range_end declared. Default is 100
range_end = 100
#global variable max_turns declared. Default is 7.
max_turns = 7
#global variable turns to keep track of the number of turns
turns = 0

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number, turns
    secret_number = random.randrange(0,range_end)
    print "\n\nStarting new game with range [ 0,",range_end,")"
    turns = max_turns
    print "You have", turns, "turns to guess!\n"
    
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game
    print "Ending current game..."
    global range_end, max_turns
    max_turns = 7
    range_end = 100
    new_game()
    

def range1000():
    # button that changes the range to [0,1000) and starts a new game
    print "Ending current game..."
    global range_end, max_turns
    max_turns = 10
    range_end = 1000
    new_game()
    
    
def input_guess(guess):
    # main game logic goes here	
    #converting guess to an integer
    global turns
    
    guess = int(guess)
    print "Your guess was", guess
    
    if(guess > secret_number):
        print "You need to guess lower"
        turns -= 1
        print "You have", turns, "turns remaining\n"
        if (not turns):
            print "Sorry, you have failed. The correct number was", secret_number
            new_game()
    elif(guess < secret_number):
        print "You need to guess higher"
        turns -= 1
        print "You have", turns, "turns remaining\n"
        if (not turns):
            print "Sorry, you have failed. The correct number was", secret_number
            new_game()
    elif(guess == secret_number):
        print "CONGRATULATIONS! YOU ARE CORRECT!"
        new_game()
        

    
# create frame
frame = simplegui.create_frame('Guess the number!',200,200)


# register event handlers for control elements and start frame
inp = frame.add_input('Guess?', input_guess, 150)
r100 = frame.add_button('Range 0 - 100', range100, 150)
r1000 = frame.add_button('Range 0 - 1000', range1000, 150)

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
