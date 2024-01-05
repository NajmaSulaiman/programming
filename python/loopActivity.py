#Q2

for i in range(1,5):
    print("*" * i)
for i in range(5,0,-1):
    print("*" * i)
    
    
    

#Q3: perfect number
number=int(input("enter a number: "))
summ=0
for i in range(1,number):
    if(number%i==0):
        summ=summ+i
        
if(number==summ):
    print ("the number is perfect")
else:
    print ("the number is not perfect")
    
summ=0
for i in range(1,101):
    for j in range(1,i):
        if(i%j==0):
            summ+=j
    print()
     
            
    if(summ ==i ):    
       print (str(i)+" is perfect")
    else:
        print (str(i)+" is not perfect")
    #to make it 0 for each number
    summ=0








        
#Q4
        
n=int(input("enter a number: "))
s=0
q=n
while(n!=0):
    p=n%10
    s+=p**(len(str(n)))
    n=n//10
if(s==q):
    print('Yes')
else:
    print('No')
    
    
n=input()
m=int(n)
s=0
q=m
while(m!=0):
    p=m%10
    s+=p**(len(n))
    m=m//10
if(s==q):
    print('Yes')
else:
    print('No')

        
        

