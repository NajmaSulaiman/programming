list_=[1,2,3]
print(list_)
#change value in list
list_[2]=4
print(list_)

list1=[1,2,3,4,5]
#print index of the list
for i in range (len(list1)):
    print(i,end=" ")
print()
#print value of list
for i in range (len(list1)):
    print(list1[i],end=" ")
print()
# print value of list without range
for i in list1:
    print(i,end=" " )
print()    
for i in [55,66]:
    print(i,end=" ")
print()
#print total of list
total=0
for i in range (len(list1)):
    total+=list1[i]
    print(total,end=" ")
print()
#print list without loop
print(list1)
#conver string o list using split
s="a,b,c"
list2=s.split(",")
print(list2)
#copy list
list3=[8,2,5,1,7]
x=list3
print(x)
#copy with change
x[4]=5
print(list3)
print(list3[-1])
print()
list4 = [1,2,3,4,-3]
counter=0
#print without list
for i in list4:
    print(int(i),end=" " )
print()
#print *2
for i in list4:   
    print(int(i)*2,end=" " )
print()
#count the negative number
for i in list4:
    if(i  <1):
        counter+=1
print(counter)
print()
#append to make new value to the list
list4.append(7)
print(list4)
print()
    
    


    
    
 





