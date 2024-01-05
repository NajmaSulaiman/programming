
#using for 
v="abaacb"
mark=6
x=input("enter your choice: ")
for i in range(len(x)):
    if( x[i]!=v[i]):
        mark-=1
       
print(mark,"out of ",len(x))


#using functuion
def grade_Exam(num_q, mark_for_each):
    
    sum_mark=0
    answer=input("enter answer for {} question:".format(num_q))  
    user_answer=input("enter your choice: ")
    for i in range(len(answer)):
        if( user_answer[i]==answer[i]):
            sum_mark+=mark_for_each
    
    print(sum_mark,"out of ",len(answer)*mark_for_each)
grade_Exam(6,2)




