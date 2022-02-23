#in dictionaries we can store any  thing
# to form dictionary
''' sushil={"sushil":"kahayat","rahyl":"subedi"} # synatax {"key":"item"}
print(sushil)


# another method to form dictionary
sus= dict(name="sushil",cast="sushil")
print(sus)
print(type(sus)) '''


#you can store list in dictionary
''' dictionary= {"num":2,"name":"sushil","list1":[1,2,3],"list2":[]}
print(dictionary["num"]) # to print data synatx = dictionary["key"]

print(type(dictionary["list1"])) # you can stor list

dictionary["list2"].append("sk") # you can add to that list
print(dictionary)
 '''
 
# you can use this pattern
''' dicti= {"name":"sushil",
        "cast":"kathayat",
    "class":"bacheoler"}
print(dicti)
  '''
  
  
# how to add in dictionay
''' empty= {}
empty["name"]= 'sushil'
print(empty)


folder= {"file":"doc","program":"python"}
folder["second"]="c"
print(folder) '''



# to check if key is exist in dic
''' dictionary= {"name":"sushil","cast":"kathayat","number":9865630920}
if 'name' in dictionary:
    print("it is ")
 '''

# to check if value is exist in dic
''' dictionary= {"name":"sushil","cast":"kathayat","number":9865630920}
if "sushil" in dictionary.values():
    print("yes") '''
    
    
    

# loop in dictionary
''' dictionary= {"name":"sushil","cast":"kathayat","number":9865630920}
for i in dictionary:
    print(i) # it will print all key
    
for i in dictionary.values(): # it will take all value
    print(i) '''
    
    

# print all values another method
''' dictionary= {"name":"sushil","cast":"kathayat","number":9865630920}
for i in dictionary:
    print(dictionary[i]) '''
    
    

# itemm() method
''' dictionary= {"name":"sushil","cast":"kathayat","number":9865630920}
for i in dictionary.items(): # it will  print one key:value as (key,value)
print(i) '''


# to print all key:value of dictionary
''' dictionary= {"name":"sushil","cast":"kathayat","number":9865630920}
for i,j in dictionary.items():
    print(f"key is{i} and value is {j}") '''
    




# add and delete item in dictionarry
# dictionary= {"name":"sushil","cast":"kathayat","number":9865630920}
# to add
''' dictionary["sex"]= "male"
print(dictionary)
 '''

''' # to remove 
remove= dictionary.pop("number") # syntax = pop("key")
print(dictionary)# it remove number:9865630920
print(remove)

# to remove random we use popitem
removerandom= dictionary.popitem()
print(dictionary)
print(removerandom) '''







# use update method
''' old_file= {"name":"sushil","cast":"kathayat","number":9865630920}
recent_file= {"adress":"anamnagar","name":"sushil kathayat","college":"LA"} # here name is two time but it will not add name again. it will update that name key
old_file.update(recent_file)
print(old_file) '''



# fromkeys method = to asign same value in different keys
''' # in list
dictionary= dict.fromkeys(["name","person","firstname"],"sushil")
print(dictionary)

# in tuple
dictionary1= dict.fromkeys(("name","first name","person"),"sushil")
print(dictionary1)

# in string
dictionary2= dict.fromkeys("abc",3)
print(dictionary2)

# in integer
dictionary3 = dict.fromkeys(range(1,11),["sushil","kathayat"])
print(dictionary3) '''




# use get() insted of dictionary["key"]
''' dictionary= {"name":"sushil","cast":"kathayat","number":9865630920}
# print(dictionary["names"]) # it give error because names is not in dictionary
# but 
print(dictionary.get("names")) # instead of eror it will return none
 '''

# exercise using get()
# dictionary= {"name":"sushil","cast":"kathayat","number":9865630920}
#type1
''' if "name in dictionary:
    print("yes")
else:
    print("no") '''
#type 2
''' if dictionary.get("name"):
    print("yes")
else:
    print("not") '''

# more about get()
''' dictionary= {"name":"sushil","cast":"kathayat","number":9865630920}
print(dictionary.get("names","not found")) # names is not in dictionary so instead of none it will git not found as output '''
    
    
    




# clear()
''' dictionary= {"name":"sushil","cast":"kathayat","number":9865630920}
dictionary.clear()
print(dictionary) '''


# to copy
''' dictionary= {"name":"sushil","cast":"kathayat","number":9865630920}
dict2= dictionary.copy()
print(dict2) '''
    
