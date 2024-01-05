from random import randint
#num1=int(input("enter a number 1-20: "))
num1=randint(1,20)
while True:
#for num in range(1,21):
    num2=int(input("enter a number 1-20: "))
    if(num1==num2):
        break
    elif(num2<num1):
        print("go up")
        continue
    
    elif(num2>num1):
        print("go down")
        continue
    
    else:
        print("try again")
        continue
print("you win")