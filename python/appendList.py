num=[]
#append(insert in the last of the list)
num.append(1)
num.append(2)
num.append(3)
num.append(4)
print("list after append: ",num)
#insert(index,element values)
num.insert(0,0)
num.insert(0,"A")
print("list after insert: ",num)
print("who is in index 3? ",num[3])
print("index of number 2? ",num.index(2))
#remove(element)
num.remove(4)
print("list after remove: ",num)
#pop(remove from the last)
num.pop()
print("list after pop: ",num)
#pop(remove using index)
num.pop(0)
print("list after index pop: ",num)
#list after change
list1=[2,4,6,8,9]
old_list=list1.pop(4)
print(list1)
#list+list
a=["a","b","c"]
b=["d","e","f"]
c=a+b
print(c)
print(c*2)
#min & max
print("max of list: ",max(["a","b","c"]))
print("min of list: " ,min(["a","b","c"]))
print(num)
print(len(num))
listA=[4,7,1,0,3]
print("list before sorting: ",listA)
listA.sort()
print("list after sorting:  ",listA)




