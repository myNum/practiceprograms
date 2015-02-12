print "A palindrome is a word, phrase, or sequence that reads the same backward as forward."

user_input = raw_input("What word would you like to test? ").lower()

reverse = user_input[::-1]

if user_input == reverse:
    isPalindrome = True
else:
    isPalindrome = False

if isPalindrome:
    print "Well, would you look at that; it's a palindrome!"
else:
    print "Sorry, Charlie, it's not a palindrome."