""" User enters three 5s then displays that fact.
Valid inputs: 0-9,(Q or q to quit)"""
list1 = []

myBoolean = 0

while myBoolean < 3:
    MyNumber = input("Please input number or Q to quit: ")
    try:
                
        if MyNumber == "5":
            intFives = int(MyNumber)
            list1.append(intFives)
            myBoolean += 1
            if len(list1) == 1:
                print("Two more please!")
            elif len(list1) == 2:
                 print("One more please!")    
            
            elif len(list1) == 3:
                print("Three 5s have been entered. Thank you!")
        else:
            crashSite = int(MyNumber)      
       
    except:        
        if len(MyNumber) != 1:
            print("invalid data...not numeric or Q")
            
        elif len(MyNumber) == 1:
            MyNumber1 = ord(MyNumber)
            
            if MyNumber1 == 113 or MyNumber1 == 81:
                print("Bye")
                break                         
            else:
                print("invalid data...not numeric or Q")
                
         
             
     
   
