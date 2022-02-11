# x= input("enter a no.")
# x= int(x)
# if x==10 or x==11:
#     print("your are correct")
# else:
#     print("you guess wrong")
    
    
    # input name and age
    # if name is start with a or A and age is above 10 
    # then print you can watch porn
    
name,age= input("enter your name and age using ,").split(",")
if name[0]=="a" or name[0]=="A":
    if int(age)>10:
        print("you can watch porn") 
else:
    print("you are banned")