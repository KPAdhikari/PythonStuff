#!/usr/bin/env python3
# https://www.youtube.com/watch?v=F6u5rhUQ6dU (at about 8:00 min)
#    Nina Zakharenko - Memory Management in Python - The Basics - PyCon 2016

x = 300
y = 300
z = 200

# Outputs from the following will show that x and y
#   refer to the same object (a storage/variable in the heap,
#   which has a value of 300 stored in it). These reference
#   variables x, y and z are located in stack but they point
#   to the objects located in the 'heap' part of the program's
#   memory space allocated by the underlying OS/platform.
print( "id(x)", id(x) )
print( "id(y)", id(y) )
print( "id(z)", id(z) )

# If they refer to the same object, it returns 'ture' else 'false'
print "'print(x is y) gives'", x is y

print("print(x is z) gives", x is z)
