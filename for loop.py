""" # 1
name= "sushil"
for i in range(10):#0 to 9
    print(name,i)# it start from 0 to 9
     """
     

#2
# if you want print starting from 1 then
""" name = "sushil"
for time in range(1,11):# initial:end-1
    print(name,time) """
    
    
    
#3 to print sum from 1 to 10
""" i= 0
for j in range(1,11):
    i=i+j
   
print(i) """

# to print from 1 to 100
""" i= 0
for j in range(1,101):# it doesnt include 101
    i+=j
    
print(i) """



# to sum natural no. from  1 to n wherer n is user input
""" no= int(input("enter your natural no"))
l= 0
for i in range(1,no+1):
    l= l+i
print(l)
 """
 
 
 # excercise
 #input no. having digit more than 1 and print the sum of digits 
 # 1234= 1+2+3+4
""" integer= input("enter more than 1 digit no.")
s= len(integer)
t= 0
for i in range(0,s):
    t+= int(integer[i])
print(t) """



#exercise 2
# input any name and print each character with its count
""" 
name= input("enter any name")
leng= len(name)
for i in range(1, leng+1):
    print(f"{name[i-1]}:{name.count(name[i-1])}")
    # it will print s:2, 2 time so below coding should be used instead """



#type 2
""" name= input("enter any name")
hey=""
leng= len(name)
for i in range(0,leng):
    if name[i] not in hey:
        hey+=name[i]
        print(f"{name[i]}:{name.count(name[i])}")
         """
