# GOAL
# Create a program that prints out every line to the song "99 bottles of beer on the wall." This should be a pretty simple program, so to make it a bit harder, here are some rules to follow.

# RULES
# 1. If you are going to use a list for all of the numbers, do not manually type them all in. Instead, use a built in function.
# 2. Besides the phrase "take one down," you may not type in any numbers/names of numbers directly into your song lyrics.
# 3. Remember, when you reach 1 bottle left, the word "bottles" becomes singular.
# 4. Put a blank line between each verse of the song.


def the_song():

    bottle_count = 99
    chorus1 = "bottles of beer on the wall."
    chorus2 = "bottles of beer. \n"
    chorus3 = "Take one down; pass it around. \n"

    while bottle_count != 2:
        print bottle_count, chorus1, bottle_count, chorus2
        print chorus3

        bottle_count = bottle_count - 1

        print bottle_count, chorus1, "\n"
        continue
            
    if bottle_count == 2:
        print bottle_count, chorus1, bottle_count, chorus2
        print chorus3

        bottle_count = bottle_count - 1

        print bottle_count, "bottle of beer on the wall. \n"

    if bottle_count == 1:
        print bottle_count, "bottle of beer on the wall.", bottle_count, "bottle of beer. \n"
        print chorus3
        print "No more bottles of beer on the wall."

the_song()
