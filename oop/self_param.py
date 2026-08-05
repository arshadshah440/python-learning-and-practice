#The self parameter is a reference to the current instance of the class.

# It is used to access properties and methods that belong to the class.

class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def greeting(self):
        print("Hello, my name is " + self.name)
        print("I am " + str(self.age) + " years old.")
        print("I am " + self.gender + ".")
        self.is_adult()
    
    def is_adult(self):
        if self.age >= 18:
            print(self.name + " is an adult.")
        else:
            print(self.name + " is not an adult.")
    
pi=Person("Arshad Shah",1,"Male")
pi.greeting();
