# to check if list have all no. even 
#if list have all true all function give true
''' list0=[True,True,True]
print(all(list0))
 '''
# but if one is false then it print false
''' list01=[True,False,True,True]
print(all(list01))
 '''

''' list1=[1,2,3,5,6,7,8]
list2=all([i%2==0 for i in list1])
print(list2) #it print false because 1 or more no. aree odd '''

#if list1 have all even no. then all function  print true






#any
''' list3=[True,True,True,True]
print(any(list3)) '''

#but any function will print true wether the list have false or not
''' list4=[True,False,False,False]
print(any(list4)) '''




#use of all any practise
#sonl1
''' def sum1(*args):
    total=0
    for i in args:
        total+=i
    print(total)
sum1(1,2,2,3,5,"sushil") # it will give error '''

#in above problem we can use any and all to manange solution
''' def sum1(*args):
    list1=all([type(i)==int for i in args])
    if list1==True:
        total=0
        for i in args:
            total+=i
        print(total)
    else:
        print("your input is wrong")

sum1(1,2,4,5)
     '''