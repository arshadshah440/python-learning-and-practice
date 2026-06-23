# A variable is created the moment you first assign a value to it.

x = "HI"

print(x)

# Variables do not need to be declared with any particular type, and can even change type after they have been set.

x= 5 

print(x)

# If you want to specify the data type of a variable, this can be done with casting.

y = int(5)
z = str(5)

print(y)
print(z)


# get the data type of a variable with the type() function.

print(type(x))
print(type(y))
print(type(z))

#Variable names are case-sensitive.

b = 50
B = "51"

print(b)
print(B)

""" 
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.

"""

name = 'Arshad'
_name = 'Arshad'
Last_name = 'Shah'
middleName= 'Hussain'  
nickname1= "Acho"

# Camel Case

firstName = "Arshad"

#pascal case 

FirstName= "Arshad"

#snake case

first_name= "Arshad"

#  assign values to multiple variables in one line:

x , y , z = "first" , "Second" , "Third"

print(x)
print(y)
print(z)

# And you can assign the same value to multiple variables in one line:

x = y = z = "Same"

print(x)
print(y)
print(z)

# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# In the print() function, you output multiple variables, separated by a comma:

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#You can also use the + operator to output multiple variables:

x = "Python"
y = "is"
z = "awesome"
print(x + y + z)

# For numbers, the + character works as a mathematical operator:

x = 3
y = 5
print(x + y )

#global variables

# Create a variable outside of a function, and use it inside the function
#If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.



x = "awesome"

def myfunc():
  x= "inner"
  print("Python is " + x)

myfunc()


# If you use the global keyword, the variable belongs to the global scope:

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)