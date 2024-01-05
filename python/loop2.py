import random
"""
for i in range(4,6):
    for j in range (1,4):
        print("{} x {} ={}".format(i, j , i*j))
        
s="hello"
for i in s:
    print(i, end=" ")
    
d="hello"
for i in range(len(d)):
    print(s[i], end=" ")
    
"""
v="aoeuiAOUEI"
counter=0
x=input("enter your full name: ")
for chr1 in x:
    if(chr1 in v):
        counter+=1
print(counter)


v="0123456789"
counter=0
x=input("enter your ID: ")
for chr1 in x:
    if(chr1 in v):
        counter+=1
print(counter)


x=random.randint(1,10)
print(x)

for i in range(1,5):
    for j in range(1,i+1):
        print(j, end=" ")
    print()




    