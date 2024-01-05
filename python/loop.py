#1 2 3 4 5
start=1
while(start <=5):
    print(start)
    start+=1
    
#eve num 2 4 6 8
start=2
while(start<10):
    print(start)
    start+=2
#sum of all number befor the num
start=1
n=int(input("enter number: "))
sumofNumber=0
while(start <=n):
    sumofNumber+=start
    start+=1
print("the sum of the number is  "+str(sumofNumber))

#sum of str
i=0
n=input("enter a number: ")
sum_=0
while(i <len(n)):
    sum_+=int(n[i])
    i+=1
print("sum of the number is : " +str(sum_))






#sum of int
# i=0
n=int(input("enter a number: "))
sum_=0
#while(i <=len(str(n))):
while(n !=0):
    sum_+=n%10
    n=n//10
    print(n)
    #i+=1
print("sum of the number is : " +str(sum_))

#break:
i=1
while(i<=6):
    print(i)
    if(i==4):
        break
    i+=1

#continue
i=0
while(i<=6):
    if(i == 4):
        i+=1
        continue
    print(i)
    i+=1
    
#while loop for secret
x="|rx#duh#juhdwh"
i=0
while(i < len(x)):
    new=ord(x[i])-3
    print(chr(new),end="")
    i+=1
    
    
#for loop
for i in range(7):
    print(i)
print("-"*10)    
for i in range(1,7):
    print(i)
print("-"*10) 
for i in range(1,7,2):
    print(i)
    
for i in range(1,5):
    print("*" * i)
for i in range(5,0,-1):
    print("*" * i)
    
    
num1=int(input("enter a number 1-20: "))
for num in range(1,21):
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
    
start=1
n=int(input("enter number: "))
sumofNumber=1
while(start <=n):
    sumofNumber*=start
    start+=1
print("the factor of the number is  "+str(sumofNumber))


factor=1
n=int(input("enter number: "))
for i in range(1,n+1):
    if(i != n):
        print(i,end="*")
    else:
        print(i)
        
    factor*=i
    
print()
print(factor)
    
    




    






    
    
