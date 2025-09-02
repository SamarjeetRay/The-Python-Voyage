#Global Variables


#Create a variable outside of a function, and use it inside the function
x= "Motki"

def myfunc():
    print("Prajukta is "+ x)

myfunc()
print()

#Create a variable inside a function, with the same name as the global variable
x = "Motki"

def myfunc():
    x = "Gadhi"
    print("Prajukta is "+x)

myfunc()

print("Prajukta is "+x)
print()


#Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

#To create a global variable inside a function, you can use the global keyword.

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
print()


#To change the value of a global variable inside a function, refer to the variable by using the global keyword:
x = "awesome"

def myfunc():
  global x
  x = "fantastic2"

myfunc()

print("Python is " + x)
print()