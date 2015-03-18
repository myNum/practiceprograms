
# Create a program that allows the user to input the sides of any triangle, and then return whether the triangle is a Pythagorean Triple or not. - Done
# Extra Credit
# If your program requires users to input the sides in a specific order, change the coding so the user can type in the sides in any order. Remember, the hypotenuse (c) is always the longest side. - Done
# Loop the program so the user can use it more than once without having to restart the program. - Done

import fractions

list = 0

def triangle_sides():
    global list
    while True:
        try:
            side1 = int(raw_input("What is the first side of the triangle that you want to check?\n"))
            side2 = int(raw_input("The second side?\n"))
            side3 = int(raw_input("And the last side?\n"))
# Checks for a GCD besides one for the three sides.
            gd = fractions.gcd(side1, side2)
            gd2 = fractions.gcd(side3, gd)
# Returns the side reduced by the GCD when applicable.
            side1r = side1 / gd2
            side2r = side2 / gd2
            side3r = side3 / gd2
            list = [side1r, side2r, side3r]
            list.sort()
            return list
        except ValueError:
            print "Your entry must be an integer."

# a = list[0]
# b = list[1]
# c = list[2]

def check():
    global list
    # Basic Pythagorean Theorem test.
    if ((list[0])**2) + ((list[1])**2) != list[2]**2:
        return False
    # C is always odd.
    if list[2] % 2 == 0:
        return False
    # Either A or B must be odd, but not both.
    elif (list[0] % 2 == 0) and (list[1] % 2 == 0):
        return False
    # Either A or B must be even, but not both.
    elif (list[0] % 2 == 1) and (list[1] % 2 == 1):
        return False
    # Either A or B must be a mutiple of 3, but not both.
    elif (list[0] % 3 == 0) and (list[1] % 3 == 0):
        return False
    # Either A or B must be a mutiple of 3, but not both.
    elif (list[0] % 3 != 0) and (list[1] % 3 != 0):
        return False
    # Either A or B must be a mutiple of 4, but not both.
    elif (list[0] % 4 == 0) and (list[1] % 4 == 0):
        return False
    # Either A or B must be a mutiple of 4, but not both.
    elif (list[0] % 4 != 0) and (list[1] % 4 != 0):
        return False
    # A and B cannot both be multiples of 5.
    elif (list[0] % 5 == 0) and (list[1] % 5 == 0):
        return False
    # One of A, B or C must be a multiple of 5.
    elif (list[0] % 5 != 0) and (list[1] % 5 != 0) and (list[2] % 5 != 0):
        return False
    elif (list[2] + list[0]) % 2 != (list[2] - list[0]) % 2:
        return False
    elif (list[2] + list[0]) % 1 != (list[2] - list[0]) % 1:
        return False
    else:
        return True

def main_function():
    while True:
        triangle_sides()
        pyth_trip = check()
        if pyth_trip == True:
            print "Looks like you discovered a Pythagorean Triple!"
        elif pyth_trip == False:
            print "Sorry, Charlie. That is not a Pythagorean Triple."
        check_again = raw_input("Do you want to check another triangle?\n").lower()
        if check_again in ["yes", "y"]:
            continue
        else:
            print "Thanks for tri-ing this program!"
            break

main_function()

# Notes on Pythagorean Triples

# At most one of a, b, c is a square.
# The area of a Pythagorean triangle cannot be the square[9]:p. 17 or twice the square[9]:p. 21 of a natural number.
# Exactly one of a, b is odd; c is odd.
# Exactly one of a, b is divisible by 3.
# Exactly one of a, b is divisible by 4.
# Exactly one of a, b, c is divisible by 5.
# The largest number that always divides abc is 60.
# All prime factors of c are primes of the form 4n + 1. Therefore c is of the form 4n + 1.


# More rules:
# An interesting fact: a Pythagorean Triple always consists of: all even numbers, or two odd numbers and an even number.
# A Pythagorean Triple can never be made up of all odd numbers or two even numbers and one odd number. This is true because:

# The square of an odd number is an odd number and the square of an even number is an even number.

# It is easy to construct sets of Pythagorean Triples.

# When m and n are any two positive integers (m < n):

# a = n**2 - m**2
# b = 2nm
# c = n**2 + m**2
