# tuples are mutable they cant be change
''' tuple1=(1,2,3,4,5,5)
print(tuple1) '''
# tuple1.append(3)  # error


# but you can asign any list inside tuples
# and you can change that list
''' tuple2=(1,2,3,4,5,[2,34,5])
tuple2[5].append(1)
print(tuple2) '''




# tuple in 1 element
''' tuple3= (4)
print(#type(tuple3))# it is not tuple you should use ,

tuple4=(4,)
print(type(tuple4)) # it is tuple
 '''
 
 
 
#tuple without parenthesis\
''' tuple5= "sushil","kathayat",1,3,5,"statement"  # it will automatically be a tuple
print(type(tuple5))
 '''
 
 
# tuple unpacking
''' tuple6= ("sushil","kathayat",5,6)
a,b,c,d= (tuple6)
print(a,b,c,d)
# it if you asign only two variable
# a,b=(tuple6)   # it will give error '''


# function that return two value
''' def twov(a,b):
    summ= a+b
    mul=a*b
    return summ,mul
print(twov(3,4)) # output=(7,12)  it doesnt give two value but one tuple

# but to print two diff value
summ,mul=twov(3,4)
print(summ) # 7
print(mul) # 12 '''




# change tuple into list
''' tuples= (1,2,24,5,6)
tuples= list(tuples)
print(tuples) '''

''' list1= [2,34,4,6]
print(tuple(list1)) # to change list into tuples '''

''' tuples3= tuple(range(1,11))
print(tuples3) '''



