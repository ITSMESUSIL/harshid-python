# *arges
# for example
''' def sum1(a,b):
    sum2= a+b
    return sum2

print(sum1(1,2)) '''
# but
# if we pass three or more input it give error
# print(sum1(1,2,3,5))


# so we use*args for multiple input inside function
''' def sum3(*args):
    print(args)
sum3(1,2,3,4,5) '''




# 2 with parameter
''' def sum4(num1,*args):
    print(num1)
    print(args)
sum4(2,3,5566,6,6) '''



#args with arguement
''' def sum5(*args):
    print(args)
list1=[1,2,3,4,5,"s"]
sum5(list1)# it will take whole list as 1
# to unpack it
sum5(*list1) '''



# exercise input a no. and list and print list**no.
''' def power(a,*args):
    if args:
        list2=[i**a for i in args]
    else:
        print("it is empty")
    return list2
list1=[1,3,4,5,7]
print(power(2,*list1))
print(power(2,*[])) '''




# args print as tuple
#kwargs= keyword arguement prints as dictionary
#to unpack list or tuple in args use *first to input
# to unpack dictionary in kwargs use **first to input


#use kwargs to print dictionary

''' def function1(**kwargs):
    print(kwargs)

function1(name="sushil",cast="kathayat") '''


#use kwargs to input any dictionary and use looping
''' dictionary1={"name":"susil","cast":"kathayat"}
def function2(**kwargs):
    for i,j in kwargs.items():
        print(f"{i} : {j}")
function2(**dictionary1) '''



# maintain order in parameter = parameter,*args,default parameter,**kwargs
''' def function3(name,*args,cast="unkown",**kwargs):
    print(name)
    print(args)
    print(cast)
    print(kwargs)
function3('sushil',1,2,3,5,nam="sushil",cas="kathayat") # dont mess with the order
 '''
 
 
 
 
 
 
# exercise input list containing strings and print first letter of string capital
''' def function4(a):
    list2=[]
    for i in a:
        list2.append(i.title())
    print(list2)
list1=["sushil","kahthayat"]
function4(list1) '''
         