# https://stackoverflow.com/questions/9079036/how-do-i-detect-the-python-version-at-runtime
from __future__ import print_function  #this must be the first import
import sys
from sys import version_info

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



"""


When you do

from __future__ import whatever

You're not actually using an import statement, but a future statement. You're reading the wrong docs, as you're not actually importing that module.

Future statements are special -- they change how your Python module is parsed, which is why they must be at the top of the file. They give new -- or different -- meaning to words or symbols in your file. From the docs:

    A future statement is a directive to the compiler that a particular module should be compiled using syntax or semantics that will be available in a specified future release of Python. The future statement is intended to ease migration to future versions of Python that introduce incompatible changes to the language. It allows use of the new features on a per-module basis before the release in which the feature becomes standard.

If you actually want to import the __future__ module, just do

import __future__

and then access it as usual.

Comment:  Technically, it is also an import statement, as the relevant name is bound to a local variable. from __future__ import print_function both changes the behavior of the print keyword and has a runtime affect equivalent to print_function =  __import__('__future__').print_function
pppery Jul 17 '17 at 1:19

"""


if version_info[0] < 3:
    print("python version = ", version_info[0])
else:
    print("python version = ", version_info[0])

# which means we don't even have to have the if-else-block:
print ("python version = ", version_info[0])
