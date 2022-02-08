from sys import set_coroutine_origin_tracking_depth


#one type
name= "sushil\t"
class2= 5
rollno=39
field= "\tscience\t" 
print( "your name is",name  +"class is",str(class2)+" "+"\trollno is,",str(rollno)+"\tyour branch is",field)

#second type
print("your name is {} class is {} \troll is {}  and branch is {}".format(name,class2,rollno,field))

# type 3
print(f"your name is {name}class is {class2}\trollno is, {rollno}\tyour branch is {field}")
 
 # excersise
one,two,three= input("enter first ,second and third no. using ,").split(",")
average =((int(one)+int(two)+int(three))/3)
print(f"your average is {average}")
print("your average is {}".format(average))




# # one more time

name = "sushil"
phoneno= 9865630920
print("your name is {} and phone number is {}".format(name, phoneno))
print(f"your name is {name} and phone number is {phoneno}")

