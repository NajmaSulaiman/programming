
# function of all functions
def main():
    result=sum_num(1,4,2)
    print(result)

#we enter number of parameter
def sum_num(a,b):
    return a+b
result=sum_num(1,4)
print(result)

#we don't enter number of parameter
def sum_num(*args):
    sum1=0
    for n in args:
        sum1+=n
    return sum1

result=sum_num(1,4)
print(result)
result=sum_num(1,4,6)
print(result)
result=sum_num(1,4,-3,2)
print(result)

main()

#this num is public
num=5
def main():
    print(func1(2),func2(1))
def func1(x):
    num=5
    return x*num

def func2(x):
    i=4
    y=3
    return i*x+y-num

main()

#sum of in using def return
n=int(input("enter a number: "))
def Sum_Digit(x):
    
    sum_=0
    i=n

    while(i !=0):
        sum_+=i%10
        i=i//10
        
    return sum_
result=Sum_Digit(n)
print("sum of the number is : " +str(result))

    
    



    
    
