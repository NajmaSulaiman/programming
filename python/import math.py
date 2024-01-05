import math
a=2
b=3

a, b= b, a 
print (a , b)
print(8//3)
print(2//5)
print(7//6)
print(math.sqrt(25))

from math import *
print(sqrt(25))
print(5%3)
a=2
b=4
t=30
print(sqrt(a**2 +b**2 - 2*a*b*cos(t)))

name= "najma"
print("Hello "+name)
age = 24
print("hello {} , age:{}" .format(name,age))
print(len("najma"))

print (name[2])
print (name.index("j"))


print("-"*50)


black=10
white=9
gap=1
blockSize=5
total_width=(black+white+gap)*blockSize
print(total_width)


print("-"*50)

total=int(input("enter number of total: "))
#total=100
blockSize=int(input("enter number OF blockSize: "))
#blockSize=5
wall=total//blockSize
print("wall :"+str(wall))
black=wall//2
white=black-1
gap=wall-(black+white)
print("Gap : "+str(gap))
print("Balck & White : " + str(black+white))



