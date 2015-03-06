
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