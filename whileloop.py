""" # sum  of no. from 1 to 10
from re import M


x= 1
y= 0
while x<=10:
    y=y+x 
    print("sum",y)
    x= x+1

    
# sum of no. from 1 to 1oo
a = 1 
b= 0
while a<=100:
    b= b+a
    a= a+1
print("your sum is ",b)

# excercise 2 take input no. from user and sum from 1 to that input no.
natural= int(input("enter the natrural no."))
l= 0
m= 1
while m<=natural:
    l= l+m 
    m= m+1
print("your sum is ",l) """


# # excercise take input number having digit more than 1 and print the sum of digits in that no.
# 1234= 1+2+3+4
# dig= input("any no. having more than one digit")
# y=int(dig)
# m=len(dig)
# a= 0 
# b= 1
# while(b<=m):
#     a=a+int(dig[b-1])
#     b= b+1
# print(a)


#exercise 3
""" take any name input
and print each character with its count"""
# name= input("enter any name")
# o= len(name)
# # a=0
# b=0
# while b<o:
#     print(f"{name[b]}:{name.count(name[b])}")
#     b=b+1
""" sushil
s:2
u:1
s:2
h:1
i:1
l:1    """
#but here s:2 is print 2 times 
# so skip repeated item the following program  is processed


# excercise
# name2= input("enter your name")
# xyz=""
# i=0
# j= len(name2)
# while i<j:
#     if name2[i] not in xyz:
#         xyz+=name2[i]
#         print(f"{name2[i]}:{name2.count(name2[i])}")
#     else:
#         i= i+1
    
    
    
#container
hey= ""
name=input("enter your name")
x= len(name)
i=0
while(i<x):
    if name[i] not in hey:
        hey=hey+name[i]
        print(name[i])
    i=i+1
    