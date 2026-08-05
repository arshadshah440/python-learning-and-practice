#All classes have a built-in method called __init__(), which is always executed when the class is being initiated.

#The __init__() method is used to assign values to object properties, or to perform operations that are necessary when the object is being created.

class Person:
    def __init__(self,name="Arshad",age=16):
        self.name=name
        self.age=age

p1=Person("Arshad Shah",19)

print(p1.name)
print(p1.age)