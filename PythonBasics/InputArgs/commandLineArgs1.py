
# https://www.geeksforgeeks.org/python-set-6-arguments/
# https://stackoverflow.com/questions/9079036/how-do-i-detect-the-python-version-at-runtime

# Python code to demonstrate the use of 'sys' module
# for command line arguments
# The first element in the list is the name of the file.
# The arguments always come in the form of a string even if we type an integer in the argument list. We need to use int() function to convert the string to integer.

from __future__ import print_function
import sys
import platform;
import six
from math import factorial
import os


#
# https://stackoverflow.com/questions/7075082/what-is-future-in-python-used-for-and-how-when-to-use-it-and-how-it-works
# The line 'from __future__ import print_function' allows the use of features
#  which will appear in newer versions while having an older release of Python
#  For example, we can use print() function even in python2
# This special line has to be at the first line of code (or import) if we
#    want to use it.
#


#__future__ is a pseudo-module which programmers can use to enable new language features which are not compatible with the current interpreter. For example, the expression 11/4 currently evaluates to 2. If the module in which it is executed had enabled true division by executing:
#
#from __future__ import division
#
#the expression 11/4 would evaluate to 2.75. By importing the __future__ module and evaluating its variables, you can see when a new feature was first added to the language and when it will become the default:
#



# command line arguments are stored in the form
# of list in sys.argv
argumentList = sys.argv

#print(platform.sys.version_info)

##https://stackoverflow.com/questions/9079036/how-do-i-detect-the-python-version-at-runtime

"""
if sys.version_info[0] < 3:
    print "Python version info: " + sys.version_info
    print argumentList

    # Print the name of file
    print sys.argv[0]

    # Print the first argument after the name of file
    print sys.argv[1]
    print "factorial(int(sys.argv[1])) = " + factorial(int(sys.argv[1]))
#else:
if sys.version_info[0] > 2:
"""

print('Python version info: ', sys.version_info)
print("argument-list: ", argumentList)

# Print the name of file
print("sys.argv[0]=", sys.argv[0])

# Print the first argument after the name of file
print("sys.argv[1]=", sys.argv[1])

print("factorial(int(sys.argv[1])) = ", factorial(int(sys.argv[1])))

dirname = os.path.dirname(__file__)
#filename = os.path.join(dirname, 'relative/path/to/file/you/want')
filename = os.path.join(dirname, '.')
print(". = ", filename)
filename = os.path.join(dirname, '..')
print(".. = ", filename)

print(sys.path.append(os.path.realpath('..')))
print(sys.path.append(os.path.realpath('.')))

print("I am at: ", os.path.dirname(os.path.realpath(__import__("__main__").__file__)))

# https://stackoverflow.com/questions/51520/how-to-get-an-absolute-file-path-in-python
#This always gets the right filename of the current script, even when it is called from within another script. It is especially useful when using subprocess.
print("This file is: ", os.path.abspath(sys.argv[0]))


"""
It also makes easier to navigate folders by just appending /.. as many times as you want to go 'up' in the directories' hierarchy.

To get the cwd:

>>> os.path.abspath(filename+"/..")
'/foo/bar'

For the parent path:

>>> os.path.abspath(filename+"/../..")
'/foo'

By combining "/.." with other filenames, you can access any file in the system.
"""


print("This is the cwd: ", os.path.abspath(sys.argv[0]+"/.."))
print("This is the parent directory: ", os.path.abspath(sys.argv[0]+"/../.."))
