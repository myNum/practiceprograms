# This is a program that tests whether a word is a palindrome or not.
print "A palindrome is a word, phrase, or sequence that reads the same backward as forward. \n"

def palindrome():

    while True:
        user_input = raw_input("What word would you like to test? ")

        palindrome_test = user_input.lower()

        reverse = palindrome_test[::-1]

        if palindrome_test == reverse:
            isPalindrome = True

        else:
            isPalindrome = False

        if isPalindrome:
            print "Well, would you look at that;", user_input, "is a palindrome! \n"
        else:
            print "Sorry, Charlie,", user_input, "is not a palindrome. \n"

        play_again = raw_input("Would you like to test another word? Y or N \n")
    
        if play_again in ["y", "Y", "yes", "YES"]:
            continue
        
        else:
            print "Ciao!"
            break

palindrome()