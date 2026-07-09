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

#bool

print(10 > 9)
print(10 == 9)
print(10 < 9)

#arithematic operator

x = 12
y = 5

print(x // y)

print(x / y)

print(x + y)

print(x - y)

print(x * y)

#The Ternary Operator

num = 6

x = "Fri" if num == 5 else "Sat" if num == 6 else "Sun" if num == 7 else "weekday"

print(x)

#Comparison Operators


x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

#The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:

print(6 & 3)

#The | operator compares each bit and set it to 1 if one or both is 1, otherwise it is set to 0:

print(6 | 3)

#The ^ operator compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0:

print(6 ^ 3)


""" Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members. """


fruits= ['banana','apple','pineapple']
print(fruits[1])
print(len(fruits))
print(type(fruits))


print(fruits[:2])
print(fruits[1:2])

if "apple" in fruits: 
   print("apple exist in list")


fruits.insert(2 , "Watermelon")

fruits.append("peach")

veg=("tomato","ladyfinger")

fruits.extend(veg)

fruits.remove("tomato")

fruits.pop(2)

del fruits[3]

newlist = [x for x in fruits if x != "apple"]


print(fruits)
print(newlist)

thislist = ["orange", "Mango", "kiwi", "pineapple", "banana"]
thislist.sort(key = str.lower)


print(thislist)

thisnum = [100, 50, 65, 82, 23]

thisnum.sort(reverse=True)


print(thisnum)


# copy the list

newlist = thisnum.copy()

listusinglist= list(thisnum)

listusingslice=thisnum[:]

print(newlist)
print(listusinglist)
print(listusingslice)


#join 2 lists

joinedlist= newlist + listusinglist

#or use the extend method

print(joinedlist)



#tuple 
#A tuple is a collection which is ordered and unchangeable.



thistuples = ("apple", "banana", "cherry")
print(thistuples)

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#unpacking a tuple

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, *yellow, red) = fruits

print(green)
print(yellow)
print(red)


#joining tuple 

newjoined= fruits + thistuples

print(newjoined)

newmultiple=fruits * 2

print(newmultiple)


#Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.

set= {'check','it','out'}

print(set)

#Add an item to a set, using the add() method:


thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

# remove and discard can be used to remove a value from the set

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")
thisset.remove("apple")

print(thisset)


""" There are several ways to join two or more sets in Python.

The union() and update() methods joins all items from both sets.

The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates. """

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
mysetunion=set1 | set2 | set3 | set4

set3 = set1 & mysetunion
set5 = set1 - mysetunion


print(myset)
print(mysetunion)
print(set3)
print(set5)

x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))

#Dictionary is a collection which is ordered** and changeable. No duplicate members.

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(thisdict)

print(thisdict['year'])
print(thisdict.keys())
print(thisdict.values())
print(thisdict.items())


#change/add the value
thisdict.update({"year": 2020})
thisdict.update({"month": "jan"})

print(thisdict['year'])

thisdict["year"] = 2022
thisdict["day"] = 23
print(thisdict['year'])
print(thisdict)

#remove the items 

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

#remove whole item 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)


#There are ways to make a copy, one way is to use the built-in Dictionary method copy().

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

#Make a copy of a dictionary with the dict() function:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

#Create a dictionary that contain three dictionaries:
#nested dictionary

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)