#excercis guess the number game
# import random
# var= random.randint(1,100)
# using for loop
""" var=10
for i in range(1,8):
    var2= int(input("enter your no"))
    if var2>var and i<6:
        print("too high")
    elif var2<var and i<6:
        print("too loow")
    elif var2 ==var and i<6:
        print("you win in")
        print(f"you guessed in {i} chance")
        break
    else:
        if var2>var:
            print("too high")
        elif var2<var:
            print("too low")
        print("you loose")
        break """


#using while loop
""" y= 10
x= 1
while True:
    var= int(input("enter any no."))
    if var>y:
        print("too high")
    elif var<y:
        print('too low')
    elif var==y:
        print("you win in",x)
        break
    x= x+1 """
    
    
    
#2nd method using while loop
""" x= 11
num= int(input("enter your no."))
y= 1
guess= False
while not guess:
    if num>x:
        print('too  high')
        num=int(input("guess again"))
        y+=1
    elif num<x:
        print("too low")
        num= int(input("guess again"))
        y+=1
    else:
        print(f"you win the game in {y} chance")
        guess = True  """
        
        
        
        
#use random 
#random.randint
""" import random
winning_num=random.randint(1,10)
i=1
num=int(input("guess"))
while True:
    if num>winning_num:
        print("too high")
    elif num<winning_num:
        print("too low")
    else:
        print(f"you win in {i}")
        break
    i=i+1
    num=int(input("guess again")) """
    
    
    
    
    
    
# using for loop and random
import random
num= random.randint(1,10)
num2= int(input('enter your guess'))
for i in range(1,10):
    if num2>num:
        print("too hig")
    elif num2<num:
        print("too less")
    else: 
        print(f"you win in {i}")
        break
    num2=int(input("guess again"))
print("you lost")
    
    
        
        
        

    