""" a= 10
def function1(b):
    a=8
    print(a)

print(a)
function1(9)# first search for local varibles
print(a)
 """
 
 
a= 10
def function1(b):
    global a  # global will change the global value inside function
    a=8
    print(a)

print(a)
function1(9)
print(a)
 