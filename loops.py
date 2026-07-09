#With the while loop we can execute a set of statements as long as a condition is true.

i=0

while i < 6:
   i+=1
   if(i == 3):
    break
   print("i value is " , i)

else: 
    print("i is not less then 6")


#A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

adj = ["red", "big", "tasty"]

for x in adj:
    print(x)
else: 
    print("loop finished")

for x in range(4,9):
    if(x==6):
        continue
    elif(x == 8) : 
        break
    print(x)
else: 
    print("loop finished")