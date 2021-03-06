# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):

seasons = ['Winter', 'Spring', 'Summer', 'Autumn']
input_month = input("Please enter the month of the year as three characters (Jan - Dec: )")

# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
input_day = int(input("Please enter the day of the month: "))

if input_month in ('Dec', 'Jan', 'Feb'):
    if input_month == 'Dec' and input_day >= 21:
        season = seasons[0]
    elif input_month == 'Dec' and input_day < 21:
        season = seasons[3]
    else:
        season = seasons[0]
elif input_month in ('Mar', 'Apr', 'May'):
    if input_month == 'Mar' and input_day >= 20:
        season = seasons[1]
    elif input_month == 'Mar' and input_day < 20:
        season = seasons[0]
    else:
        season = seasons[1]
elif input_month in ('Jun', 'Jul', 'Aug'):
    if input_month == 'Jun' and input_day >= 21:
        season = seasons[2]
    elif input_month == 'Jun' and input_day < 21:
        season = seasons[1]
    else:
        season = seasons[2]
elif input_month in ('Sep', 'Oct', 'Nov'):
    if input_month == 'Sep' and input_day >= 21:
        season = seasons[3]
    elif input_month == 'Sep' and input_day < 21:
        season = seasons[2]
    else:
        season = seasons[3]
print(f"{input_month} {input_day} is in {season}")

  

# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall



# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 
# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.
