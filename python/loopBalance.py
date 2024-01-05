
pin=0
balance=100
while(pin == pin):
    
    
    if (pin == 1234 ):
        choose=int(input("""choose what you want:
                1-check balance
                2-withdraw money
                3-deposit money
                 :"""))
        if (choose ==1):
            print("your final balance is :  "+str(balance))
            break
        elif(choose==2):
            withdrow=int(input("enter how many withdrow you want:"))
        
            print("your final balance is :  "+str(balance-withdrow))
            break
        elif(choose==3):
            deposit=int(input("enter how many deposit you want: "))
            print("your final balance is :  "+str(balance+deposit))
            break
        else:
            print("Try again please")
            break
                
    
                  
    else:
        print("You Enter wrong pin")
        

