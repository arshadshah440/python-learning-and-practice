""" Python allows for user input.

That means we are able to ask the user for input. """

print("Multply 2 number /n");

print("enter your first number")

x= input("enter your number:")

print("enter your second number")

y= input("enter your number:")

try: 
    if(int(x) and int(y)):
        print("your results are ", int(x) + int(y),".");
except:
    print("kindly enter integers numbers")