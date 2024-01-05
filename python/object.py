s="Makeen"
print(s.upper())
print(s.lower())
print(s.replace("e","a"))
print(s.replace("e","a",3))
print(s[3])
print(s.find("M"))
print(s.find('e',2))
print(s.find('e',10))
print(s.count("e"))
print(s[::-1])
print(s[::-3])
print(s[:-3])
print(s[:-1])

#char

x= "a"
y= "n"
print(ord(x))
print(ord(y))

str1= "my isname isisis jameis isis bond";
sub="is";
print(str1.count(sub,4))

#input and output
Firstname= input("please enter your name")
print ("your name is "+ Firstname)
bornYear=int(input("please enter your born year"))
print("your age is  "+ str(2023-bornYear))

#formatted ourput

price= 1.21997
print("the price %0.2f " %(price))

total= 34.21997
print("the total %-10s " %(total))
number=int(input("enter a number "))
print("%04d" %(number))
age=2023-bornYear
print(Firstname +"%4d" %(age))






                
