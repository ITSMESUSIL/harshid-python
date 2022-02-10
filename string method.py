intro= "sushil KAthYaT IS mOsT FamOuS PerSOn"
    # len()
print(len(intro))
print(len("housefull"))

# upper()
x=intro.upper()
print(x)

# lower()
y= intro.lower()
print(y)

# title
t= intro.title()
print(t)

# count()
print(intro.count("s"))


 
name= "katHayat"
print(len(name))
print(name.upper())
print(name.lower())
print(name.title())
print(name.count("a"))

excercise
name,cast= input("enter your name and cast using ,").split(",")
hey= input('enter the character you want to count')
print(len(name))
print(name.count(hey))

name,char= input("enter the name and character using,").split(",")
print(f"your string length is {len(name)} and your word count is {name.upper().count(char.upper())}")

name= "SksSSkK"
yellow="k"
print(f"your count is {name.lower().count(yellow.lower())}")



