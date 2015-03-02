# Rock-paper-scissors-lizard-Spock


print "This is the more advanced version of rock, paper, scissors. This game also includes lizard and Spock."
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random

def name_to_number(name):
    if name is "rock":
        return 0
    elif name is "Spock":
        return 1
    elif name is "paper":
        return 2
    elif name is "lizard":
        return 3
    elif name is "scissors":
        return 4
    else:
        print "That is not an acceptable option for RPSLS"

def number_to_name(number):
    if number is 0:
        return "rock"
    elif number is 1:
        return "Spock"
    elif number is 2:
        return "paper"
    elif number is 3:
        return "lizard"
    elif number is 4:
        return "scissors"
    else:
        print "That is not an acceptable option for RPSLS"


def rpsls():
    # print out the message for the player's choice
    player_choice = raw_input("What would you like to play?\n")
    print "You chose:", player_choice
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    # print out the message for computer's choice
    print "Computer chooses:", comp_choice
    # compute difference of comp_number and player_number modulo five
    difference = comp_number - player_number
    # use if/elif/else to determine winner, print winner message
    if difference == 0:
        print "Tie!"
    elif difference <= 2:
        print "You wins!"
    elif difference > 2:
        print "Ah, bummer; computer wins!"

# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls()

