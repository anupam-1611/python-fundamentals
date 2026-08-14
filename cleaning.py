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
