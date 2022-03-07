# zip is used to combine two or more lists or tuple
''' name=["sushil",'rahul',"asif"]
cast= ["kathayat","subedi","ansari"]
zip1=list(zip(name,cast))
print(zip1)
 '''

#tuple
''' tuple1=(1,3,5,7)
tuple2=(2,4,6,8)
zip2=list(zip(tuple1,tuple2))
print(zip2) '''

#[(sushil,kathayt),(rahul,subedi )] you can convert this type of list into dictionary
''' list1=[("sushil",'kathayat'),("rahul","subedi")]
print(dict(list1)) '''



# you can zip two lists to make dictionary
''' list1=["name","class","course"]
list2=["sushl","bacheoler","it"]
zip2=dict(zip(list1,list2))
print(zip2) '''