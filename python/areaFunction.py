import math
n=int(input("enter the number of side: "))
s=float(input("enter the side: "))
def area(n,s):
    
    area=((n*s**2)/(4* math.tan((22/7)/n)))
    
    return area
result=area(n,s)
print("The area of the polygon is ",result)
print("The area of the polygon is ",round(result,2))