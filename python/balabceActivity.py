from sys import exit
pin="1234"
balance=100
userpin=input("enter your pin:")
if (pin == userpin):
    choose=int(input("""choose what you want:
                1-check balance
                2-withdraw money
                3-deposit money
                 :"""))
    if (choose ==1):
        print(balance)
    elif(choose==2):
        withdrow=int(input("enter how many withdrow you want:"))
        
        print("your final balance is :  "+str(balance-withdrow))
    elif(choose==3):
        deposit=int(input("enter how many deposit you want: "))
        print("your final balance is :  "+str(balance+deposit))
    else:
        print("Try again please")
                
    
                  
else:
    exit("You Enter wrong pin")
