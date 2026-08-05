#Properties are variables that belong to a class. They store data for each object created from the class.

class Person:
    gender="Male"

    def __init__(self,name,age):
        self.name=name
        self.age=age

p1=Person("John Doe",19)
p2=Person("John",16)
print(p1.name)

p1.age=20
print(p1.age)

del p1.age

print(p1.gender)
Person.gender="Female"

print(p2.gender)
print(p1.gender)



#print(p1.age)