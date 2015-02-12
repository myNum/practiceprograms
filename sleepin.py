
day_of_week = raw_input("What day of the week is tomorrow? ").lower()

if day_of_week == "saturday" or "sunday":
    sleepin = True
else:
    sleepin = False

if sleepin:
    print "Lucky you! It looks like you're sleeping in tomorrow!"
else:
    print "Sucks to be you! Looks like you're getting up early tomorrow!"