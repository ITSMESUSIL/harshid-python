#1 input=3 then output= {1:1,2:8,3:27}
''' def cubefinder(a):
    dictionary={}
    for i in range(1,a+1):
        dictionary[i]=i**3
    return dictionary
print(cubefinder(3))
         '''

# 2 take input name,age,fav_movie as list,fav_music as list and print key:value in different line
''' dictionary={}
name,age= input("enter your name and age ").split(",")

age=int(age)
dictionary["name"]=name
dictionary["age"]=age
fav_movi= input("enter movie name using ,")
fav_musi= input("enter music name using ,")
fav_movie=fav_movi.split(",")
fav_music= fav_musi.split(",")
dictionary["fav_movie"]= fav_movie
dictionary["fav_music"]= fav_music
print(dictionary)
for i,j in dictionary.items():
    print(i,j)
 '''