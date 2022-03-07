# choose only even numbers from the list
''' list3= [1,2,3,4,5,6,6,7]
def filter2(a):
    if a%2==0:
        return a
filter3=list(filter(filter2,list3))
print(filter3)
# map and filter
map1=list(map(filter2,list3))
print(map1) '''


# shortcut to solve using lambda function
''' list3=[1,2,3,4,5,6,7]
lambda1=lambda a:a%2==0
filter3= list(filter(lambda1,list3))
print(filter3 ''')

# make list of a word from string
name="kathayat"
list1=[]
for i in name:
    if i=="a":
        list1.append(i)
print(list1)

# using filter function 
list2=[]
for i in name:
    list2.append(i)
def filter1(i):
    if i =="a":
        return i
filter2=list(filter(filter1,list2))
print(filter2)
    
    