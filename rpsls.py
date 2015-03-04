# Rock-paper-scissors-lizard-Spock


print "This is the more advanced version of rock, paper, scissors. This game also includes lizard and Spock.\n"
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random

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

def player_shoots():
    name = raw_input("What would you like to play?\n").lower()
    print "\nYou chose:", name
    while True:
        if name == "rock":
            return 0
        elif name == "spock":
            return 1
        elif name == "paper":
            return 2
        elif name == "lizard":
            return 3
        elif name == "scissors":
            return 4
        else:
            name = raw_input("That's not an acceptable answer. You must chose one of the five options.\n")
            print "You chose:", name
            continue


def computer_shoots():
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    # print out the message for computer's choice
    print "\nComputer chose:", comp_choice, "\n"
    return comp_number

def rpsls():
    difference = (player_shoots() - computer_shoots()) % 5
    # use if/elif/else to determine winner, print winner message
    if difference == 0:
        print "Tie!"
    elif difference <= 2:
        print "You win!"
    elif difference > 2:
        print "Ah, bummer; computer wins!"
    play_again = raw_input("\nWould you like to play again? Y or N \n").lower()
    if play_again in ["y", "yes"]:
        rpsls()
    else:
        print "Thanks for playing!"
rpsls()

