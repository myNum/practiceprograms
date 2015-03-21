# Goal Create a program that allows the user to input the total weight of each type of coin they have (pennies, nickels, dimes, and quarters), and then print out how many of each type of wrapper they would need, how many coins they have, and the estimated total value of all of their money.
# Weight of each coin and how many fit inside each type of wrapper.
# Subgoals
# Round all numbers printed out to the nearest whole number.
# Allow the user to select whether they want to submit the weight in either grams or pounds.

# Penny = 2.5g, 50 per roll, $0.50, total weight per roll: 125g
# Nickel = 5.0g, 40 per roll, $2.00, total weight per roll: 200g
# Dime = 2.268g, 50 per roll, $5.00, total weight per roll: 112.4g
# Quarter = 5.67g, 40 per roll, $10.00, total weight per roll: 226.8g

# 100g = 0.22lbs

def get_unit():
    weight_type = raw_input("Would you like to use grams or pounds as your weight unit?").lower

    if weight_type in [gram, grams, g]:
        return grams
    if weight_type in [pound, pounds, lb, lbs]:
        return pounds

def get_weights():
    print "Please enter the total weight for each of the following coins.\n"
    penny_weight = raw_input("Pennies:\n")
    nickel_weight = raw_input("Nickels:\n")
    dime_weight = raw_input("Dimes:\n")
    quarter_weight = raw_input("Quarters:\n")

def number_wrappers():
    penny_wrappers = penny_weight / 125
    nickel_wrappers = nickel_weight / 200
    dime_wrappers = dime_weight / 112.4
    quarter_wrappers = quarter_weight / 226.8
