""" 
Python supports the usual logical conditions from mathematics:

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b """

day = 3

if day == 1:
  print("Monday")
elif day == 2:
  print("Tuesday")
elif day == 3:
  print("Wednesday")
elif day == 4:
  print("Thursday")
elif day == 5:
  print("Friday")
elif day == 6:
  print("Saturday")
else:
  print("Sunday")


a = 2
b = 330
print("A") if a > b else print("B")

#mutliple condition
a = 330
b = 390
print("A") if a > b else print("=") if a == b else print("B")

#and operator

a = 200
b = 33
c = 500
if a > b and a > c:
  print("All of the conditions is True")

#or operator

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

#not operator
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

#nested if statement

score = 92
extra_credit = 5

if score >= 90:
  if extra_credit > 0:
    print("A+ grade")
  else:
    print("A grade")
elif score >= 80:
  print("B grade")
else:
  print("C grade or below")

#pass

age = 16

if age < 18:
  pass # TODO: Add underage logic later
else:
  print("Access granted")

#match 

day = 8
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")
  case _: 
    print("default")