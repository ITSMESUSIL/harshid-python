# map
# for example
list1= [1,2,3,4,5]
# print its squares
list2=[]
for i in list1:
    list2.append(i**2)
print(list2)

# using map it will easier
# actually you can use map instead of list comprehension
def function1(a):
    return a**2
numbers=tuple(map(function1,list1))
print(numbers)


list4=["sushil","kathayat","last"]
print(map(len,list4))





# another
list5=[1,2,3,4,5,6,7,8]
def oddeven(a):
    if a%2==0:
        return a
even= list(map(oddeven,list5))
print(even)
# it include none so we use filter
