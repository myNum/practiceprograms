
# Create a program that allows the user to input the sides of any triangle, and then return whether the triangle is a Pythagorean Triple or not.
# Extra Credit
# If your program requires users to input the sides in a specific order, change the coding so the user can type in the sides in any order. Remember, the hypotenuse (c) is always the longest side.
# Loop the program so the user can use it more than once without having to restart the program.

def pyth_check(a, b, c):
    a = raw_input("What is the first side of the triangle you want to check?\n ")
    b = raw_input("The second side?\n ")
    c = raw_input("And the third side? n")

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
