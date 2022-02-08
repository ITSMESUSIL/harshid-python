name= input("enter your name")
age= input ("enter your age")
# print(name+age)

#but you can do in one line
name,age= input("enter your name and age").split()# use .split()
print(name)
print(age)

#2
question,answer= input("write the question and aswer").split(",")
print(question)
print(answer)

