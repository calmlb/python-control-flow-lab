# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 
while True:
    phrase = input('Please enter a word or phrase or type the word "Quit" to exit.')
    if phrase == "Quit":
        break
    else: 
        print (phrase)
        length = len(phrase)
        print (length)
        lengthInt = str(length)
        print (lengthInt)
        print ('What you entered is ' + lengthInt + ' characters long.')
        
# 2. Print the following message:

        


#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.

