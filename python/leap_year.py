
userYear=int(input("enter a year: "))
if(userYear % 400 ==0) and ( userYear% 100 ==0 ):
             print( str(userYear)+" is a leap year")
elif(userYear % 4 ==0) and ( userYear% 100 !=0 ):
             print( str(userYear)+" is a leap year")
else:
             print( str(userYear)+" is not a leap year")

print(2020%400)
print(2020%4)
print(2020%100)