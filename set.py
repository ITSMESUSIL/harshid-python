# set store only unique items
set1={1,2,3,4,5,5,56} # it will remove another 5
print(set1)

# convert a list into set
list1=[1,2,34,5,6,9]
set2=set(list1)
print(set2)

#add in set
list3={2,3,4,5,6}
list3.add(9)
print(list3)

# remove from set1
set1.remove(3)
print(set1)

set1.discard(56)
print(set1)

# intersection and union in set
# for union
a={2,3,4,5,6,7}
b= {3,4,5,9,10}
union= a|b
print(union) # {2,3,4,5,6,7,8,10}
# for intersection
print(a & b) # {3,4,5}