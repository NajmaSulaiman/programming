
def shape1(x,a):
    traiangle=(b*h)/2
    return traiangle

def shape2(z,r):
    sqrr=b*h
    return sqrr

def shape3(y):
    cirle=(22/7)*(n**2)
    return cirle

def shape4(w,s):
    cylinder=(2*(22/7)*(n**2))+(2*(22/7)*n*h)
    return cylinder

choose=0
while (choose==choose):
    choose=int(input("enter 1,2,3,4,5(for quiting): "))
    if(choose==1):
        b=int(input("enter number height : "))
        h=int(input("enter number base : "))
        result =shape1(b,h)
        print("the Area of triangle: "+str(result))
    elif(choose==2):
        b=int(input("enter number height : "))
        h=int(input("enter number base : "))
        result =shape2(b,h)
        print("the Area of Square: "+str(result))
    elif(choose==3):
        n=int(input("enter number radius : "))
        result =shape3(n)
        print("the Area of cirle:  "+str(result))
    elif(choose==4):
        n=int(input("enter number radius : "))
        h=int(input("enter number height : "))
        result =shape4(n,h)
        print("the Area of cylinder: "+str(result))
    elif(choose==5):
        print("exit")
        break
        
        
    