"""
Python has the following data types built-in by default, in these categories:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType

"""

#Try it
x = "Hello World"	#str	
x = 20	#int	
x = 20.5	#float	
x = 1j	#complex	
x = ["apple", "banana", "cherry"]	#list	
x = ("apple", "banana", "cherry")	#tuple	
x = range(6)	#range	
x = {"name" : "John", "age" : 36}	#dict	
x = {"apple", "banana", "cherry"}	#set	
x = frozenset({"apple", "banana", "cherry"})	#frozenset	
x = True	#bool	
x = b"Hello"	#bytes	
x = bytearray(5)	#bytearray	
x = memoryview(bytes(5))	#memoryview	
x = None

# Numbers

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# random

import random

print(random.randrange(1, 10))


#strings

x= """Hi! it's working,
you should test it."""

print(x)
print(x[1])
print(len(x))

#not/in  is case sensitive

print("Working" not in x)


#slicings

a = "Hi!Myname is Arshad"

print(a[0:8])

print(a[:8])

print(a[8:])

print(a[-5:-1])

#modify string

a = "Hello, World!"

print(a.lower())

print(a.upper())

print(a.strip())

print(a.replace("H", "J"))

print(a.split(",")[1])

# String Concatenation

a = "Hello"
b = "World"
c = a + b
print(c)

#F-Strings

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

#The escape character allows you to use double quotes or any restricted character when you normally would not be allowed:


txt = "We are the so-called \"Vikings\" from the north."
print(txt)
