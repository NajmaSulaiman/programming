h1=int(input("enter a hour for first time :"))
m1=int(input("enter a min for first time :"))
ampm1=input("input am or pm for first time :")

h2=int(input("enter a hour for second time :"))
m2=int(input("enter a min for second time :"))
ampm2=input("input am or pm for second time :")

if(ampm1 == "am" and ampm2 =="pm"): 
    print ("first time is first :"+ str(h1)+":"+str(m1)+ampm1)
elif (ampm2 == "am" and ampm1 =="pm"):
    print ("second  time is first  "+ str(h2)+":"+str(m2)+ampm2)
else:
    
    if (h1 < h2):
        print("first time is first  "+ str(h1)+":"+str(m1)+ampm1)
    elif(h1 == h2):
        if (m1<= m2):
            print ("first time is first  "+ str(h1)+":"+str(m1)+ampm1)
        else:
            print ("second  time is first  "+ str(h2)+":"+str(m2)+ampm2)
            
    else:
        print ("second  time is first  "+ str(h2)+":"+str(m2)+ampm2)
    
    
    


