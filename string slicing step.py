name = "sushil"
print(name[::2])# syntax[initial:endpoint:step]  it means print the string step ahead
print(name[4:6])
print(name[5::-1])# -1 will print letter step down by 1
print(name[-1::-1])


#excercise
name=input("enter your name ",)
print(f"your reverse is {name[-1::-1]}")
print("your reverse is {}".format(name[-1::-1]))
