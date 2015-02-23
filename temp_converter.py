# This program allows users to convert the temperature from Celsius to Fahrenheit and vice versa.

def get_temp():
    temp = int(raw_input("What temperature would you like to convert? \n> "))
    return temp

def temp_converter():

    while True:

        c_or_f = raw_input("Would you like to convert to Celsius or to Fahrenheit? (C or F) \n> ").lower()
        
        try:
            if c_or_f in ["c", "celsius"]:
                # c = 5 / 9 * (f - 32)
                converted_temp = 5.0 / 9.0 * (get_temp() - 32)
                print "The temperature in Celsius is", converted_temp, "degrees."
                break
    
            elif c_or_f in ["f", "fahrenheit"]:
                # f = 9 / 5 * C + 32
                converted_temp = 9.0 / 5.0 * get_temp() + 32
                print "The temperature in Fahrenheit is", converted_temp, "degrees."
                break
        
            else:
                print "Please choose C for Celsius or F for Fahrenheit."
                # continue
                # This still works with "continue" commented out. Why?

        except ValueError:
            print "Your entry must be a number."
            # continue
            # This still works with "continue" commented out. Why?
            
    another_temp = raw_input("Would you like to calculate another temperature? (Y or N) \n> ").lower()

    if another_temp in ["y", "yes"]:
        temp_converter()
    
    else:
        print "Thanks for converting!"

temp_converter()

# Items remaining include: If ValueError, determine a way to ask the user for the temperature and not start back over at chose between c_or_f. I've tried puting c_or_f above the while True, but if the program runs "else", the program returns a continuous loop of "Please choose C for ..." requiring a keyboard interuption to quit the program.