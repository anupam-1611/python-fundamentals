'''
STRING Datatype: Methods(belongs to an object) 

#using variables and f-strings

print("My name is Anupam") #without variables
print("Anupam loves Python")

#with variable
name = "Anupam"
language = "Python"
print(name, " is my name")
print(name, "loves ", language)

#with f-string
print(f"My name is {name}")
print(f"{name} loves {language}")


#Escape Sequences: Python ignores the charater after backslash

print("Line1\nLine2") # n: new line 
print("Hi\tEveryone") # t: tab(4 spaces)
print("Path: C:\\Users") #\\: ignore\\
print("She said \"Hi\"") 


#String: types & math

name = "anupam"
age = 22

print(type(name))          # type: check datatype
print("Age: " + str(age))  # str: convert int or float into string
print(len(name))           #len: count characters in a string
print(name.count("a"))     #count(""): frequency of a substring


#String transformation

date = "2026/05/10"
print(date.replace("/","-"))
#replaces certain text to another

first = "Anupam"; last = "Dutta"
print(f"{first} {last}")

cssv = "Anupam,22,India"
print(cssv.split(","))
#creates a list

print("=" *20)

# path = "C:single_backslash User" << this rasies unicode error
path = "C:\\User"
print(path)


code = "AnupamDutta-22"

print(code[0])   #"A" beacause indexing starts with 0 

print(code[-1])  #2 because starts from the back of the string[starts from right]

print(code[0:6]) # Starts from 0 and ends in 5th Index [start:end]

print(code[-5:]) #starts from -2 i.e, T[starts from right] and ends at the last cuz no value given

datee = "2026-5-29"

print(datee[0:4], datee[5:7], datee[-5:])

print(code[:10:2]) #stride  [start:end:step]
# starts at 0 and ends at 10th posi and also jumps 2 steps 


#strings cleaning

name = "  Anupam       "

print(name.strip())
print(name.lstrip())
print(name.rstrip())
#strip removes whitespace: l for left and r for right

print("$Anupam$$$$$".strip("$"))
#removes specific character from the data

search = "EMAIL"
data = " email"

print(search.lower().strip() == data.lower().strip())
#we edited(lowered and removes the whitespaces) the text inside both variables then compared both variables using comparison operator 



#strings searching: startswith,endswith, find

phn = "+91 9876543210"
print(phn.startswith("+91"))    #returns boolean

file = "data_backup.txt"
print(file.endswith(".txt"))    #returns boolean

email = "anupamduttahcs@gmail.com"
print(email.find("@")) #shows position
print("@" in email)    #returns boolean

#use find() to slice dynamically
print(phn[phn.find("-")+1:])


#strings: validate,join, format

print("India".isalpha())
print("12345".isnumeric())

parts = ["2026", "08", "18"]
print("-".join(parts)) #concatenate

print("Hi {n}, order {o}".format(n="Sam", o=1))

print("42".zfill(5)) #turns into 5 digit: 00042: fills 0's before str

'''