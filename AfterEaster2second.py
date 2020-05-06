strData = None
myBoolean = True # For my second loop
secondBoolean = True


while strData != 'Quit':
    strData = str(input("Please enter some text or enter 'Quit' to quit: "))
    if strData != 'Quit':

        myBoolean = True   # reset Value of myBoolean back to True to continue the loop.      
        strData1 = strData.lower() # convert userinput to all lowers to compare, no matter if they use upper or lowercases.

# Loop to remove commas and spaces, manly for multiple word Palindromes like (Red rum, sir, is murder)

        while secondBoolean is True:
            if ',' in strData1:
                strData1 = strData1.split(',')
                strData1 = "".join(strData1)
            elif " " in strData1:
                strData1 = strData1.split()
                strData1 = "".join(strData1)
                secondBoolean = False
            else:
                secondBoolean = False
        
        
        strReverseData = strData1[::-1] 
        intHalfsOfData = round(len(strData) / 2, ) #to display specific versions of the word
       
        if strData1 == strReverseData:
            print("Your text is a Palindrome")
        else:
            print("Your text is not a Palindrome")
            
        print("\n")
        
        print("Choices to display your text: Regular, Reverse, First half, Last half.")

        while myBoolean is True:        

            strChoice = str(input("Enter your choice: "))
        
            if strChoice == "Regular" or strChoice == "regular":
                print("The text you entered is:", strData)
                myBoolean = False
            
            elif strChoice == "Reverse" or strChoice == "reverse":
                print("The text you entered in reverse is:", strData[::-1])
                myBoolean = False
            
            elif strChoice == "First half" or strChoice == "first half":
                print("The first half of", strData,"is:", strData[0:intHalfsOfData])
                myBoolean = False
            
            elif strChoice == "Last half" or strChoice == "last half":
                print("The last half of", strData, "is:", strData[intHalfsOfData:])
                myBoolean = False
            else:
                print("invalid answer. Choices to choose from: Regular, Reverse, First half, Last half.")
               
