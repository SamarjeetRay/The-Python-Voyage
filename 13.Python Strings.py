'''Strings'''

print("Hello")
print('Hello')
print()

#You can use quotes inside a string, as long as they don't match the quotes surrounding the string:
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')
print()

#Assigning a string to a variable is done with the variable name followed by an equal sign and the string:
a = "Hello"
print(a)
print()

#ou can assign a multiline string to a variable by using three quotes:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
print()

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
print()



'''Strings are Arrays'''
#Get the character at position 1 (remember that the first character has the position 0):
a = "Hello, World!"
print(a[1])
print()

#Since strings are arrays, we can loop through the characters in a string, with a for loop.

for x in "banana":
  print(x)
print()

#The len() function returns the length of a string:
a = "Hello, World!"
print(len(a))
print()

#To check if a certain phrase or character is present in a string, we can use the keyword in.
txt = "The best things in life are free!"
print("free" in txt)
print()

#Use it in an if statement:
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
print() 

#To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
txt = "The best things in life are free!"
print("expensive" not in txt)
print() 

#Use it in an if statement:
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")