# Global variables can be used by everyone, both inside of functions and outside.
x = "Love"
def myfunc():
    print("I "+x, "you")
myfunc()

# Create a variable inside a function, with the same name as the global variable
x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x)

# If you use the global keyword, the variable belongs to the global scope:
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)