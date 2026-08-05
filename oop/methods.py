#Methods are functions that belong to a class. They define the behavior of objects created from the class.

class Calculator:
    def add(self,a,b):
        return a+b

    def subtract(self,a,b):
        return a-b

    def multiply(self,a,b):
        return a*b

    def divide(self,a,b):
        if b==0:
            return "Cannot divide by zero"
        else:
            return a/b

calc=Calculator()
print(calc.add(5,3))

class Main_Calculator:
    def __init__(self,a,b,operation):
        self.a=a
        self.b=b
        self.operation=operation
    
        
    def add(self,a,b):
        return a+b

    def subtract(self,a,b):
        return a-b

    def multiply(self,a,b):
        return a*b

    def divide(self,a,b):
        if b==0:
            return "Cannot divide by zero"
        else:
            return a/b
    
    def __str__(self):
        if self.operation=="add":
            return str(self.add(self.a,self.b))
        elif self.operation=="subtract":
            return str(self.subtract(self.a,self.b))
        elif self.operation=="multiply":
            return str(self.multiply(self.a,self.b))
        elif self.operation=="divide":
            return str(self.divide(self.a,self.b))
        else:
            return "Invalid operation"

calc1=Main_Calculator(6,3,"subtract")
print(calc1)