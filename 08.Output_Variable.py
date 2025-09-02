#The Python print() function is often used to output variables.

x = "Python is awesome1"
print(x)
print()

#In the print() function, you output multiple variables, separated by a comma:
x = "Python"
y = "is"
z = "awesome2"
print(x, y, z)
print()

#you can also use the + operator to output multiple variables:
x = "Python "
y = "is "
z = "awesome3"
print(x+y+z)
print()

#Notice the space character after "Python " and "is ", without them the result would be "Pythonisawesome".
x = "Python"
y = "is"
z = "awesome3"
print(x+y+z)
print()


#For numbers, the + character works as a mathematical operator:
x = 5
y = 10
print(x + y)
print()

#ERROR!!
#x = 5
#y = "John"
#print(x + y)


#NO ERROR:
x = 5
y = "John"
print(x, y)
print()

