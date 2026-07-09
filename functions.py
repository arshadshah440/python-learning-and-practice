
#In Python, a function is defined using the def keyword, followed by a function name and parentheses:

def my_function():
  print("Hello from a function")

my_function()


""" Function names follow the same rules as variable names in Python:

A function name must start with a letter or underscore
A function name can only contain letters, numbers, and underscores
Function names are case-sensitive (myFunction and myfunction are different) """


def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

#return the value 
def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message)

#Mixing Positional and Keyword Arguments


def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)

#To specify positional-only arguments, add , / after the arguments:



def my_function(name, /):
  print("Hello", name)

my_function("Emil")


#To specify that a function can have only keyword arguments, add *, before the arguments:

def my_function(*, name):
  print("Hello", name)

my_function(name = "Emil")

#Combining Positional-Only and Keyword-Only

def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)

#The *args parameter allows a function to accept any number of positional arguments.



def my_function(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total

print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5))

#The **kwargs parameter allows a function to accept any number of keyword arguments.



def my_function(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print(" ", key + ":", value)

my_function("emil123", age = 25, city = "Oslo", hobby = "coding")

#changecase/decorator

def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

print(myfunction())

#lambda
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

#Recursion

def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))


#generator

def large_sequence(n):
  for i in range(n):
     yield i

# This doesn't create a million numbers in memory
gen = large_sequence(1000000)
print(next(gen))
print(next(gen))
print(next(gen))