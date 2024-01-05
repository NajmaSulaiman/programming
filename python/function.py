def CubVolune (sidelength):
    volume=sidelength **3
    return volume
    
print(CubVolune(3))

#return
def grade_vrg(x):
    summ=0
    for i in range(1,x+1):
        grade=float(input("enter your grade: "))
        summ+=grade
    
    avg= summ/x
    #print("avrage os the student is "+str(avg))
    return avg
result=grade_vrg(2)
print(result)


#not return
num=int(input("enter a number :"))
def check(x):
    
        if(x%2==0):
            print("number is even")
            
        else:
            print("number is odd")
            
    
#when there are no return we don't need to print it
check(num)

#with return
num=int(input("enter a number :"))
def check(x):
    
        if(x%2==0):
            return "even"
            
            
        else:
            return "odd"
            
    
n=check(num)
print(n)
