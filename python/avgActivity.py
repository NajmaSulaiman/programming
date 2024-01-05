"""
summ=0
student=int(input("Number of student: "))
for i in range(1,student+1):
    grade=float(input("enter your grade: "))
    summ+=grade
    
avg= summ/student
print("avrage os the student is "+str(avg))
    
 """       
        
"""
summ=0
#student=int(input("Number of student: "))
for i in range(1,100):
    grade=float(input("enter your grade: "))
    summ+=grade
    stop=input("do you want to get the avrage (y/n): ")
    if(stop=="y"):
        avg= summ/i
        print("avrage of the student is "+str(avg))
        break
    else:
        continue
    """
    

#student=int(input("Number of student: "))
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
     

    

    

    