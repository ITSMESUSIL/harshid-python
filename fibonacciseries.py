#fibonacci means 0,1,1,2,3,5,8,13,21 = third no. will be sum of first two numbers
def febonacci(x):
    a= 0
    b= 1
    if x==1:
        print(a)
    elif x==2:
        print(a,b)
    else:
        print (a,b,end=" ")
        for i in range(2):
            c=a+b
            a=b
            b=c
            print(b,end=" ")
    
num=int(input("enter any num"))
febonacci(num)

