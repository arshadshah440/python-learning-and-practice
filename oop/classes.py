# Python is an object oriented programming language.

# Almost everything in Python is an object, with its properties and methods.

# A Class is like an object constructor, or a "blueprint" for creating objects.

class MyClass:
  x = 5

x=MyClass();
y=MyClass();
z=MyClass();

print(x.x)
print(y.x)
print(z.x)

del x;

#empty class

class EmptyClass:
  pass