# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age in human years like this:
#      Input a dog's age in human years: 

age = input("Input a dog's age in human years: ")

# 2. Calculates the equivalent dog years, where:

age_int = int(age)
if age_int <= 2:
    dog_age = age_int * 10
    dog_age_str = str(dog_age)
    print("The dog's age in human years is " + dog_age_str + "years old.")
elif age_int > 2: 
    dog_age = (20 + ((age_int-2) * 7))
    dog_age_str = str(dog_age)
    print("The dog's age in dog years is " + dog_age_str + ".")


#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx

# Hint:  Use the int() function to convert the string returned from input() into an integer