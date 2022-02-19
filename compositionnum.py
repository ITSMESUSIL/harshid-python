        
def primecom(x):
    y=0
    for i in range(1,x+1):
        if x%i==0:
            y=y+1
    if y>2:
        print("it composite")
    else:
        print("it is prime")
        
        
def oddeven(x):
    if x%2==0:
        print("it is even")
        primecom(x)
    else:
        print('it is odd')
        primecom(x)
x=int(input("enter your no."))
if x>=1:
    print("positive")
    oddeven(x)
elif x<=-1:
    print("negative")
    oddeven(-x)
else:
    print("neutral")
    print("it is neither even nor odd")
    print("it is neither prime nor composite")