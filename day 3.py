'''
#Numeric Types in Python: int, float, complex

x = 5
y = 3.14
z = 3 + 2j
print(type(x))
print(type(y))
print(type(z))

#Arthematic operators

a = 10
b = 5

print(a + b) 
print(a - b)
print(a * b)
print(a / b) #float
print(a // b) #remainder
print(a % b) #modulas: remainder
print(a ** b) #power: 1 to the power of b


#Comparison and Logical Operators
x = 10
y = 3

#Comparison
print(x == y)
print(x != y)
print(x > y)
print(x <= y)

# Logical
print(x>5 and x<5)
print(x< 5 or y> 0)
print(not(x == y)) # not changes the output: true=false, false=true
y = 10
print(not(x == y)) #x = 10, y = 10

#Rounding (Math Module)
import math
x = 10
y = 3

#ceil()
print(math.ceil(4.2))
print(math.ceil(4.8))
#floor()
print(math.floor(4.2))
print(math.floor(4.8))
#round(): not in math library 
print(round(y))
print(round(x))



#round function always goes to the closest even number (if .5 is the case)
print(round(1.5))
print(round(2.5))
print(round(3.5))
print(round(4.5))

import math as m

#floor(down to earth): always comes below
print(m.floor(1.2))
print(m.floor(1.5))
print(m.floor(1.7))

#ceil(attitude): always comes upward
print(m.ceil(1.2))
print(m.ceil(1.5))
print(m.ceil(1.7))



#numbers
x = [1,2,3,4]
#strings
y = ["Anupam", "Somnath", "Manish", "Shivank"]
#booleans
status = [True, False, True]
#mixed data
d = ["Anupam", 22, True]
print(d)
print(d[1])

'''

#list operations
names = ["Anupam", "Shivank", "Somnath", "aaaaa"]
print("Original names: ", names)

names.append("Manish") #adds to the end
print("After appending Manish", names)
names.remove("aaaaa") # deletes element named
print(names)
names.pop(1) #deletes element with index
print(names)