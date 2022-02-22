# reverse the taken list using append() andd pop()
""" list= [1,2,3,4,5]
list1=[]
for i in range(0,len(list)):
    x=list.pop()
    list1.append(x)
print(list1)

     """
    
# using reverse()
""" list=[1,2,3,4,5]
def reverse(o):
    list.reverse()
    return list 
print(reverse(list)) """






#input['abc','tuv','xyz']= output['cba','vut','zyx']
#type 1 using list[0]
""" list= ['abd','tuv','xyz']
def revers(l):
    list1=[]
    for i in list:
        x=i[::-1]
        list1.append(x)
    return list1
print(revers(list))
         """
         
 
 
 
 
 
# [1,2,3,4,5,6,7]= [[1,3,5,7],[2,4,6]
""" list= [1,2,3,4,5,6,7]
list1=[]
x=list[0:7:2]
y=list[1:7:2]
list1.append(x)
list1.append(y)
print(list1) """







#another question is take two list and print the common number in those list
''' list1= [1,2,3,4,5,6,7]
list2= [2,3,4,7,8,9]
def common(a,b):
    x=0
    list=[]
    for i in a:
        if a[x] in b:
            list.append(a[x])
            x=x+1
        else:
            x=x+1
            continue
    return list
print(common(list1,list2))
 '''







# last exercise
#take any list having multiple list inside and print how many 
# list are inside
''' list1= [1,2,[1,2,3],4,[5,6,7]]
if type(list1)==list:
    print("list ho")
 '''
 
# to check how many list are in given list 
''' list1= [1,2,[1,2,3],4,[5,6,7]]
def listcount(l):
    num=0
    for i in list1:
        if type(i)==list:
            num+=1
    return num
print(listcount(list1))    
    
 '''