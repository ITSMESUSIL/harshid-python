""" def function1(name,cast,age):
    print(name)
    print(cast)
    print(age)
function1("sushil","kathayat",18) """


""" def function1(name,cast,age):
    print(name)
    print(cast)
    print(age)
function1("sushil","kathayat",)# it will give error
 """
 
 
 
""" def function1(name,cast,age=19):# it is default parameter in absence of input
    print(name)
    print(cast)
    print(age)
function1("sushil","kathayat",) """




""" 

def function1(name,cast,age=10):
    print(name)
    print(cast)
    print(age)
function1("sushil","kathayat",18)# it will replace default parameter """


""" 
def function1(name,cast="unknown",age):
    print(name)
    print(cast)
    print(age)
function1("sushil",,18) # last variable can only be default otherwise it gives error """


def function1(name="unknown",cast="unknown",age="unknown"):
    print(name)
    print(cast)
    print(age)
function1()#but you can make all variable unknown
