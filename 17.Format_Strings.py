#we cannot combine strings and numbers like this:
#age = 36
#This will produce an error:
#txt = "My name is John, I am " + age
#print(txt)

'''
But we can combine strings and numbers by using f-strings or the format() method!

'''

#Create an f-string:

age = 36
txt = f"My name is John, I am {age}"
print(txt)
print()
