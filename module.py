# To create a module just save the code you want in a file with the file extension .py:

import mymodule

x= mymodule.addition(3,5);
print(x)


import platform
x = platform.system()
print(x)

import platform

x = dir(platform)
#print(x)


from mymodule import person1

print (person1["age"])


#dates modules
import datetime

x = datetime.datetime.now()
print(x.year)
print(x.strftime("%x"))

x = datetime.datetime(2018, 6, 15)
print(x.strftime("%x"))

import camelcase

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))