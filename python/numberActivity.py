"""
v="0123456789"
counter=0
x=input("enter your ID: ")
for chr1 in x:
    if(chr1 in v):
        counter+=1
print(counter)
"""
"""
om="967"
num=int(input("enter a number: "))
for num1 in num:
    if(num1 in om):
        if
        
    
    
    else:
        print("Valid number")
    """

om="968"
num=input("enter a number: ")   
if(num[0] == "+"):
    #num=input("enter a number: ")
    if((num[1:4]) in om):
        if(len(num)==12 and num[1:13].isdigit()):
            print(num[0:4]+" "+num[5:9]+"-"+num[8:12])
            
        else:
            print("wrong")
            
    else:
        print("you need start with +968")
        
else:
    print("wrong you need to start with +")
        
        
