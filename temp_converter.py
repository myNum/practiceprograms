# This program allows users to convert the temperature from Celsius to Fahrenheit and vice versa.

def temp_converter():
    
    c_or_f = raw_input("Would you like to convert to Celsius or to Fahrenheit? (C or F) \n> ").lower()
    
    temp = int(raw_input("What temperature would you like to convert? \n> "))
    
    if c_or_f in ["c", "celsius"]:
        # c = 5 / 9 * (f - 32)
        converted_temp = 5.0 / 9.0 * (temp - 32)
        print "The temperature in Celsius is", converted_temp, "degrees."
    
    elif c_or_f in ["f", "fahrenheit"]:
        # f = 9 / 5 * C + 32
        converted_temp = 9.0 / 5.0 * temp + 32
        print "The temperature in Fahrenheit is", converted_temp, "degrees."
    
    another_temp = raw_input("Would you like to calculate another temperature? (Y or N) \n> ").lower()

    if another_temp in ["y", "yes"]:
        temp_converter()
    
    else:
        print "Thanks for converting!"

temp_converter()

# Items remaining include: 1. Handling a ValueError when a non-int is entered for temp 2. Error handling for if user does not enter C or F. 