#to print no from 1 to 10
#but we want print upto 5 only then we can use break
for i in range(1,11):
    if i==6:
        break
    print(i)
    
    
#continue
#print no from 1 to 10
# but we want to skip no. 5 then use continue
for i in range(1,11):
    if i==5:
        continue
    print(i)