
# https://www.geeksforgeeks.org/python-set-6-arguments/

#Python | Set 6 (Command Line and Variable Arguments)

#Previous Python Articles (Set 1 | Set 2 | Set 3 | Set 4 | Set 5)
#This article is focused on command line arguments as well as variable arguments (args and kwargs) for the functions in python.
#Command Line Arguments

#Till now, we have taken input in python using raw_input() or input() [for integers]. There is another method that uses command line arguments. The command line arguments must be given whenever we want to give the input before the start of the script, while on the other hand, raw_input() is used to get the input while the python program / script is running.

#For example, in the UNIX environment, the arguments ‘-a’ and ‘-l’ for the ‘ls’ command give different results.

#The command line arguments in python can be processed by using either ‘sys’ module or ‘argparse’ module.



# Python code to demonstrate the use of 'sys' module
# for command line arguments

import sys

# command line arguments are stored in the form
# of list in sys.argv
argumentList = sys.argv
print argumentList

# Print the name of file
print sys.argv[0]

# Print the first argument after the name of file
print sys.argv[1]


OUTPUT :

['program1.py', 'test', '1']
program1.py
test

NOTE : The above code runs only on command line. We need to fire the below command given that the program is saved as program1.py
python program1.py test 123

Please note the following points about the above program :

    The sys.argv takes the command line arguments in the form of a list.
    The first element in the list is the name of the file.
    The arguments always come in the form of a string even if we type an integer in the argument list. We need to use int() function to convert the string to integer.

     
    We can use the command line arguments to write the programs which do frequently used tasks. For example, we need to find factorial many times. We can keep the following program in a file named factorial.py in our computer and get the output by simply writing the command for getting the factorial of a number, say 5.
    python factorial.py 5


import sys 
from math import factorial 
  
print factorial(int(sys.argv[1])) 

 
Variable Arguments
args(*) and kwargs(**)

Both ‘args’ and ‘kwargs’ are used to get arbitrary number of arguments in a function.

args will give us all the function parameters in the form of a list and kwargs will give us all the keyword arguments except for those corresponding to formal parameter as dictionary.


# Python program to illustrate the use of args which 
# multiplies all the values given to the function as parameter 
  
def multiplyAll(*values): 
    mul = 1 
  
    # values(args) will be in the form of tuple 
    print values 
    print "Type = ", type(values) 
  
  
    # Multiplying the all the parameters and return the result 
    for i in values: 
        mul = mul * i 
  
    return mul 
  
  
# Driver program to test above function 
  
# Multiply two numbers using above function 
ans = multiplyAll(1,2) 
print "The multiplication of 1 and 2 is ", ans 
  
# Multiply 5 numbers using above function 
ans = multiplyAll(3, 4, 5, 6, 7) 
print "The multiplication of 3 to 7 is ", ans 

OUTPUT :

(1, 2)
Type =  
The multiplication of 1 and 2 is  2
(3, 4, 5, 6, 7)
Type =  
The multiplication of 3 to 7 is  2520

Note that args are denoted by using a single star and kwargs are denoted by two stars before the formal parameters in the function.


# Program to illustrate the use of kwargs in Python 
  
# Function that print the details of a student 
# The number of details per student may vary 
def printDetails(**details): 
      
    # Variable 'details' contains the details in the 
    # form of dictionary 
    print "Parameter details contains"
    print details  
    print "Type = ", type(details) 
  
    # Print first name  
    print "First Name = ", details['firstName'] 
  
    # Print the department of student 
    print "Department = ", details['department'] 
    print "" # Extra line break 
  
  
# Driver program to test above function 
  
# Calling the function with three arguments 
printDetails(firstName = "Nikhil",  
             rollNumber = "007", 
             department = "CSE") 
  
# Calling the function with two arguments 
printDetails(firstName = "Abhay", 
             department = "ECE") 

Output:

Parameter details contains
{'department': 'CSE', 'rollNumber': '007', 'firstName': 'Nikhil'}
Type =  
First Name =  Nikhil
Department =  CSE

Parameter details contains
{'department': 'ECE', 'firstName': 'Abhay'}
Type =  
First Name =  Abhay
Department =  ECE

 
Please note that if you are using both args and kwargs in a function then the args parameter must precede before the kwarg parameters.
Example :


# Function containing both args and kwargs 
def cheeseshop(kind, *arguments, **keywords): 
    print "-- Do you have any", kind, "?"
    print "-- I'm sorry, we're all out of", kind 
    for arg in arguments: 
        print arg 
    print "-" * 40
    keys = sorted(keywords.keys()) 
    for kw in keys: 
        print kw, ":", keywords[kw] 
  
# Driver program to test above function 
cheeseshop("Burger", "It's very funny, sir.", 
           "It's really very, VERY funny, sir.", 
           shopkeeper='Michael Palin', 
           client="John Cleese", 
           sketch="Cheese Shop Sketch") 



This article is contributed by Nikhil Kumar Singh
 
Please write comments if you find anything incorrect, or you want to share more information about the topic discussed above
