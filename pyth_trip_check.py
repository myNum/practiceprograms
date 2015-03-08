
# Create a program that allows the user to input the sides of any triangle, and then return whether the triangle is a Pythagorean Triple or not.
# Extra Credit
# If your program requires users to input the sides in a specific order, change the coding so the user can type in the sides in any order. Remember, the hypotenuse (c) is always the longest side.
# Loop the program so the user can use it more than once without having to restart the program.
a = 0
b = 0
c = 0

def triangle_sides():
    global a, b, c
    a = int(raw_input("What is the shortest side of the triangle you want to check?\n"))
    b = int(raw_input("The middle side?\n"))
    c = int(raw_input("And the longest side?\n"))
    return a, b, c

def c_odd():
    global a, b, c
    if c % 2 == 0:
        return False
    elif (a % 2 == 0) and (b % 2 == 0):
        return False
    elif (a % 5 == 0) and (b % 5 == 0):
        return False
# this is causing 3, 4, 5 to return the wrong result.
#   elif (a % 5 != 0) and (b % 5 != 0):
#       return False
    else:
        return True

triangle_sides()

pyth_trip = c_odd()

if pyth_trip == True:
    print "Looks like you discovered a Pythagorean Triple."
elif pyth_trip == False:
    print "Sorry, Charlie. That is not a Pythagorean Triple."

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

# a = n2 - m2
# b = 2nm
# c = n2 + m2
