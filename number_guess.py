import random

def number_guess():
    comp_number = random.randint(1, 10)
    user_number = int(raw_input("I'm thinking of a number between 1 and 10. Take a guess. \n"))
    while user_number != comp_number:
    
        if user_number < comp_number:
            print "No way, Jose, that is too low."
            user_number = int(raw_input("Guess again. \n"))

        if user_number > comp_number:
            print "Woah, that is too high."
            user_number = int(raw_input("Try again. \n"))
    else:
            print "WINNER! You guessed correctly"

    play_again = raw_input("Would you like to play again? Y or N \n")

    if play_again in ["y", "Y"]:
        number_guess()

    else:
        print "Until next time!"

number_guess()

