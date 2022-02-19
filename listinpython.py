# list=["sushil","kathayat",9884,9848,9865]
# print(list[0])
# print(list[-1])
# print(list[0:2])
# print(list[-1:0:-1])

# it [initial:final-1]
# it will replace position 0 only
''' list[0:1]="rahul","subedi"
print(list)
 '''
 
#it will change position 2 only
''' list[2]= '9815'
print(list)
 '''
# it will replace 1 position with all this
''' 
list[1]=["sus","h","il"]
print(list) '''

# to change whole list

''' list[:]=["k","t","z"]
print(list)
 '''
 
 
 # use
 # insert(),extend(),append()= to add item
 # remove(),del[],pop()= to remove item
 
 
 
 
 # to add in list
''' list=["bread","coke","water"]
list.append("sigret")
print(list) '''

''' list=[]
list.append("hair dryer")
print(list)
list.append("wifi")
print(list) '''



# using insert()add some string between 
''' list= ["door","window","doorbell","wire"]
list.insert(0,"lets start")# it will insert "lets start" in position 0
list.insert(1,"inside room")
print(list) '''



# add 2 lists
''' list1= ["fruits","kota factory"]
list2=["dar lagyo","madarchod"]
list= list1+list2
print(list) '''


#use extend
''' list1=["kota","factory"]
list2= ["euta","dammi","movie"]
list1.extend(list2)
print(list1)
list1.append("ho")
print(list1)
list2.extend(list1)
print(list2)
list2.insert(0,"iron man")
list2.insert(3,"ho")
print(list2) '''


#diffrence between append and extend
''' list1=["tu","kamina","hai"]
list2=["or","kamina","hi "]
list3=["rahega"]
list1.append(list2)# it will add whole list
print(list1)
list1.extend(list3)# it will extend the list
print(list1) '''



# to remove item
''' list=["mai ","yeh","cheez","remove","karta ","hu"]
list.pop()# it will delet last item default
print(list)
list.pop(-2)# it can remove any item
print(list)
del list[0]
print(list)
del list[1]
print(list)
#if you dont know the position

list.remove("yeh")
print(list)
list.append("hu")
print(list)
list.remove("karta ")
print(list) '''



# some other methods that can be used
list= ["messi","neymar","embabbe","verane"]
list.sort()# it will arrage list in alphabetical order
print(list)
print(list)
list1=["a","c","d","b"]
print(sorted(list1))# it will change format but not permanent
print(list1)
list.clear()
print(list)
copy=list1.copy()
print(copy)
print(list1)
