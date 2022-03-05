# enumerate function is used with for loop
# it is used to determine the position and string  in list
''' list1=["sushil","kathayat"]
a=0
for i in list1:
    print(f"{a}--->{i}")
    a=a+1 '''
    
# type 2
list1=["sushil","kathayat"]
for i,j in enumerate(list1):
    print(f"{i}--->{j}")