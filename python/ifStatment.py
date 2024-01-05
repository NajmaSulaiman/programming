
number= int(input("enter a number :"))

if ((number%2)==0) :
    print("number is even")
    
else :
    print ("number is odd")
    
    
    
total_amount = int(input("enter your amount :"))
 
if total_amount > 100:
     new_amount=total_amount-(total_amount*0.10)
     
else: 
    new_amount=total_amount-(total_amount*0.05)
    
print("total of new amount : "+ str(new_amount))


gender=input("enter your gender(m or f):")
if (gender == "m" or  gender == "M"):
    age = int(input("enter your age :"))
    if( 24<age <30):
        print("accept the job")
    else:
        print("reject")
else:
    print ("reject")
    



s="h"
message="hello"
print(s in message)
print(s not in message)
x="dgd6453"
print(x.isalnum())
print(x.isdigit())
a="    "
print(a.isspace())




