# make function that input some and print last characte
""" def char(a):   # here a:is called parameter  and sk:arguement
    return a[-1]
sk= input('enter your name')
print(char(sk)) """



# make function that input any number and print wheather the  no. is even or odd
""" def even_odd(num):
    if num%2==0:
        return "even"
    else:
        return "odd"
a=int(input('enter any number'))
print(even_odd(a)) """

  #second type 
  #without using else
""" def even_odd(a):
    if a%2==0:
        return "no. is evem"
    return "no. is odd"
print(even_odd(int(input('enter your no'))))  """



#empty parameter
""" def function():
    return "hey you"
print(function())
print(function())
# print(function(9)) """




# make function that shows which no. greater
""" def greater(a,b):
    if a>b:
        return a," is greater"
    return b," is greater"
x,y=input("enter two number a,b").split(",")
print(greater(int(x),int(y))) """



# which is greater among three numbers
""" def greater(a,b,c):
    if a>b>c:
        return a
    elif b>a>c:
        return b
    return c 
x,y,z= input("enter three num a,b,c").split(",")
numb=greater(int(x),int(y),int(z))
print(f"{numb} is greater than all") """



# function inside function example
""" def great(a,b):
    if a>b:
        return a 
    return b

def greatest(a,b,c):
    num=great(a,b)
    num2=great(num,c)
    return num2
print(greatest(1,2,3)) """



#excercise is string palindrome eg: madam=madam
""" def is_palindrome(name):
    if name[:]==name[len(name)::-1]:
        return "is palindrom"
    return "is not palindrom"
name=input('enter the name')
name= name.replace(" ","")
print(is_palindrome(name)) """


#is true or not
""" def palindrom(name):
    return name==name[::-1]
print(palindrom("sushil"))#false
print(palindrom("naman"))#true """




