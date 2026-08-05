""" Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class. """

class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        print("Hello, my name is " + self.name)
        print("I am " + str(self.age) + " years old.")

class Child(Parent):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school

    def greetings(self):
        super().greeting()
        print("I go to " + self.school + " school.")

p1 = Parent("Arshad Shah", 19)
p1.greeting()

c1 = Child("Arshad Shah", 19, "ABC")
c1.greetings()