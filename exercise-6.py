# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):

seasons = ['Winter', 'Spring', 'Summer', 'Autumn']
input_month = input("Please enter the month of the year as three characters (Jan - Dec: )")
print (input_month)

# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
input_day = str(input("Please enter the day of the month: "))
print (input_day)

# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
if input_month in ('Jan', 'Feb', 'Mar'):
    season = seasons[0]
    print(input_month + input_day + " is in season " + season + ".")

elif input_month in ('Apr', 'May', 'Jun'):
    season = seasons[1]
    print(input_month + input_day + " is in season " + season + ".")

elif input_month in ('Jul', 'Aug', 'Sep'):
    season = seasons[2]
    print(input_month + input_day + " is in season " + season + ".")
else:
    input_month in ('Oct', 'Nov', 'Dec')
    season = seasons[3]
    print(input_month + input_day + " is in season " + season + ".")

# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 
# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.