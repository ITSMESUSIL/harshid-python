# list coprehension is used to make code shorter
# for example
# to print square of 1 to 10
# method 1
''' list1=[]
for i in range(1,11):
    list1.append(i**2)
print(list1) '''

# method 2
''' list1=[i**2 for i in range(1,11)] # it is shorter
print(list1) '''



# print integers from 1 to 10 in -form
''' list2= [-i for i in range(1,11)]
print(list2) '''


# make a list that in which 1st char of string taken
''' list3= ["sushil","rahul","ashif"]
list4= [x[0] for x in list3]
print(list4) '''



# exercise  make function that take list and return reverse of each component
''' list1= ["sushil","kathayat","23"]
list3=["sushil",]
def reverse(a):
    list2=[i[::-1] for i in a]
    return list2
print(reverse(list1))
print(reverse(list3))
 '''
 
 
 


# if else 
# print even numbers from 1to 10
# method 1
''' list1=[]
list2=[]
for i in range(1,11):
    if i%2==0:
        list1.append(i)
    else:
        list2.append(i)
print(list1,list2) '''

# method 2
''' list1= [i for i in range(1,11) if i%2==0] # even
list2= [i for i in range(1,11) if i%2!=0] # != is meant not equals to
print(list1,list2) '''





# exercise input any list but that make another list of only int or float numbers but that list will take int as string
# list1=["suhil","nam",3,4,4.3,"9"]
# method 1
''' def intfloat(a):
    intfloat=[]
    for i in a:
        if type(i)==int or type(i)==float:
            intfloat.append(str(i))
    return intfloat
print(intfloat(list1)) '''

# method 2
''' def intfloat(a):
    list1=[str(i) for i in a if type(i)==int or type(i)==float]
    return list1
print(intfloat(list1)) '''



# list comprehension in if and else both
# exercise from 1 to 10 if no is odd then print it in - but if it is even print it by multiply by 2
# list1= list(range(1,11))
''' list2=[]
for i in list1:
    if i%2==0:
        list2.append(i*2)
    else:
        list2.append(-i)
print(list2)
         '''
# method 2
''' list2=[i*2 if i%2==0 else -i for i in list1]
print(list2) '''