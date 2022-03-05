# lambda can be used as function
# type 1
''' def add(a,b):
    print(a+b)

add(3,5) '''


#type 2
''' funct=lambda a,b:a+b
print(funct(3,4)) '''


#function to multiply three no
''' function2=lambda a,b,c:a*b*c
print(function2(3,5,6)) '''

# make function to find wether the no. is even or odd
#type1 
''' def odd_even(a):
    return a%2==0

print(odd_even(3))
print(odd_even(4)) '''

#type 2
''' function3= lambda a:a%2==0
print(function3(4)) '''


# make a function that input a string and print its last letter
#type 1
''' def last_le(a):
    print(a[len(a)-1])
last_le("sushil")
 '''

#type 2
''' function5=lambda a:a[len(a)-1]
print(function5("kathayat")) '''


# lambda in if else
# find even or odd
''' def oddeven(a):
    if a%2==0:
        print("it is evne")
    else:
        print("it is odd")
oddeven(8) '''


# type2
''' function6=lambda a:"it is even" if a%2==0 else "it is odd"
print(function6(9)) '''