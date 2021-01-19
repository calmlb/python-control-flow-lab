# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.

#choose nth term
n = int(input("Please enter a number (n)"))
#first two terms
n1, n2 = 0, 1
count = 0

if n == 1:
    print(n1)
else: 
    print ("Fibonacci sequence")
    while count < n:
        # print first term
        print ("term: " + str(count) + " / number " + str(n1))
        # create nth case
        nth = n1 + n2
        #replaces values in lower term to next number
        n1 = n2
        #replaces n2 with nth 
        n2 = nth
        #increments to next number
        count += 1
        



# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hint: The next number is found by adding the two numbers before it
