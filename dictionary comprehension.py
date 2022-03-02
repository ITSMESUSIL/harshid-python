# print = 1:1**2
# method 1
''' def dictionary1(a):
    dictionary={}
    for i in a:
        dictionary[i]=i**2
    return dictionary
list1=list(range(1,11))
print(dictionary1(list1)) '''

# method 2
''' dictionary= {i:i**2 for i in range(1,11)}
print(dictionary) '''


# if else used
#method 1
''' dictionary={}
for i in range(1,11):
    if i%2==0:
        dictionary[i]="even"
    else:
        dictionary[i]="odd"
print(dictionary) '''

# method2
''' dictionary= {i:"even" if i%2==0 else "odd" for i in range(1,11)}
print(dictionary) '''
