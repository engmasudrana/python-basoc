'''
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
'''

'''
Python has no command for declaring a variable.
A variable is created the moment you first assign a value to it.
'''
x = 5
y = "Masud Rana"
print(x)
print(y)

# Variables do not need to be declared with any particular type, and can even change type after they have been set.
a = 4       # x is of type int
a = "salary" # x is now of type str
print(a)

# If you want to specify the data type of a variable, this can be done with casting.
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# You can get the data type of a variable with the type() function.
x = 5
y = "Love"
print(type(x))
print(type(y))

# Variable names are case-sensitive.
a = 4
A = "Sally"
#A will not overwrite a

# Python allows you to assign values to multiple variables in one line:
x,y,z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# you can assign the same value to multiple variables in one line:
x = y = z = "Orange"
print(x)
print(y)
print(z)

