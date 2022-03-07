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
    list3=[]
    list3.append(a**2)
    return list3
map(function1,list1)


list4=["sushil","kathayat","last"]
prin(map(len,list4))
