'''

#Python
print("World Hello!")
print("Python welcomes Anupam!")


#Variable: stores data, dynamic
name = "Anupam Dutta"
age = 22
print("Hi! My name is ", name, "I am ", age, "years old.")

#Dynamically typed: can be changes later
age = 32
print("After 10 years I'm gonna be", age)

x = "Hello"
print(type(x))

x = 100
print(type(x))

name = "Anupam"
print(name)
name = "Dutta"
print(name)

a = 10
b = 20
c = a + b
print(c)


#Datatype
a = 10    #integer
b = 3.14  #float
c = "Anupam"  #string
d = True   #boolean
e = None  #Nonetype

print(a)
print(b)
print(c)
print(d)
print(e)

#Dynamic: a was int then changes to str
a = "Anupam"
print(a)


#Primitive and Collection: can store one value or multiple
x = 10
y = "Anupam"
z = None

#these contain multiple values 
nums = [1,2,3,4] #list
pair = (1,2,3)  #tuple
uniq = {1,2,3,4}  #set
info = {"a": 1}     #dict

print(type(nums))
print(type(pair))
print(type(uniq))
print(type(info))


#Escape, mix, triple, tip
print("HI  \"Python\"  ")
print('HI "Python"')
print("""HI

Python!
""")


#Functions: Built-in, External(numpy, pyspark, pandas, matplotlib(these all nees import))

#built-in(len, print, type, input)
print(len("Python"))

#external
import math
print(math.sqrt(25))

#user-defined
def greet(name):
    print("hi", name)
print(greet("Anupam"))    


#user-input: always returns a string from user
name = input("Enter your name: ")
print("Heyyyy!", name)


#print(): communicate, display, debug, test

print("Anupam")
print("Sum: ", 10 + 5)
print("Yayy! Done")


total_qty = 35
price = 100
revenue = price * total_qty
print (revenue)
print("""Learning path:
Python Basics
-Data Engineering
-AI Engineering""")

#input(): pause, prompt, returns string, convert

name = input("Enter your name: ")
print("Hello,", name)

# Read a number
age = int(input("Your age: "))
print("After 10 year:", age + 10)


#Functions vs Methods
#Standalone vs Class-Bound
#Function: print(), type(), len()
#Methods: text.upper(), text.lower()

text = "Anupam"
num = 900

# Functions work on either
print(type (text))
print(len(text))

# Methods class-specific
print(text.upper())
print(num.bit_length())

# num.upper() -> Attribute Error
# int object has no attribute upper()


'''