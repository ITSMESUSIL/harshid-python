""" a= "  sushi  "# strip() to remove string sides space
b= "   sushil"# lstip() to remove string left side's space
c="sushil    "# rstip() to remove string right side's space
d= "sus  hil "# replace(" ","") to remove all space's in string
e="......"
print(a+e)
print(a.strip())
print(b)
print(b.lstrip())
print(c+e)
print(c.rstrip()+e)
print(d+e)
print(d.replace(" ","")+e) """

# excercise
""" take two input name and one character
then print length of name and how many time the character repeated in that name"""

name,char=input("enter your name and chara using , in mid").split(",")
""" suppose
Sushil,s= 5,1
Sushil, s= error due to space
Sushil, s = eroor due to space
so we have to make string space less"""
name= name.lower().replace(" ","")
char= char.lower().replace (" ","")
print(f"your name is {name} and your count is {name.count(char)}")