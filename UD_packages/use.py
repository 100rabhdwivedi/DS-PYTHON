# modules are the collection of functions, classes, and variables that are defined in a file.
# we can use the functions, classes, and variables defined in a module by importing the module


# import the strfunc module
import strfunc
from numoperation import add, sub


print(strfunc.upper("hello world"))  # Output: HELLO WORLD
print(add(5, 3))  # Output: 8
print(sub(5, 3))  # Output: 2


