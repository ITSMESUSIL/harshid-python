string= "my self sushil kathayat"
print(string.replace("my self","my name"))
str2= "he is two years old and he is so cute"
print(str2.replace("is","was"))
print(str2.replace("is","was",1))# it will replace only one is
print(str2.replace('is','was',2))# it will replace two is


#find()
str3= "she is so beutifull and is very cute"
print(str3.find("is"))
print(str3.find("is",0))
print(str3.find("is",4))
print(str3.find("is",5))# it will count after count 5
