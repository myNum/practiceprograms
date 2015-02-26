import random

def number_guess():
    while True:
        comp_number = random.randint(1, 10)

        while True:
            try:
                user_number = int(raw_input("I'm thinking of a number between 1 and 10. Take a guess. \n"))

                while user_number != comp_number:
                    if user_number < 1:
                        print "You're not good with instructions, are you? Your guess is BELOW the range of 1 tO 10."
                        user_number = int(raw_input("Guess a number that is 1 or above, and 10 or below. \n"))

                    elif user_number < comp_number:
                        print "No way, Jose, that is too low."
                        user_number = int(raw_input("Guess again. \n"))

                    elif user_number > 10:
                        print "Yo! Learn to read. Your guess is ABOVE the range 1 to 10."
                        user_number = int(raw_input("Guess a number that is 10 or below, and 1 or above. \n"))

                    elif user_number > comp_number:
                        print "Woah, that is too high."
                        user_number = int(raw_input("Try again. \n"))
                else:
                    print "WINNER! You guessed correctly."
                    break

            except ValueError:
                print "Dude, enter a NUMBER!"

        play_again = raw_input("Would you like to play again? Y or N \n").lower()

        if play_again in ["y", "yes"]:
            continue
        
        else:
            print "Until next time!"
            break

number_guess()

#Items remaining: Change how the program continues if the exception is encountered. It works fine today, but I believe there is a better way to handle this.