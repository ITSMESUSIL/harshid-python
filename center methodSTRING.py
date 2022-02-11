name= "sushil"
print(name.center(8,"*"))# just write intiger above your word count to print in center between * ---- *sushil*
print(name.center(7,"&"))# it will print one & in first
print(name.center(10,"("))

#excercise 
# take any input and print in between of 8 *
input1= input("enter your string")
y= len(input1)
print(input1.center(y+8,"*"))
print(input1[-1])
