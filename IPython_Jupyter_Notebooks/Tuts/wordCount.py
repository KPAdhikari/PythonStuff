#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#kp: 4/8/18: https://www.ntu.edu.sg/home/ehchua/programming/webprogramming/Python1_Basics.html#zz-10.4
#    Author of the article was suggesting to name it as wc.py but I chose wordCount.py

"""
wc - word count
~~~~~~~~~~~~~~~
Read a file given in the command-line argument and print the number of
lines, words and characters - similar to UNIX's wc utility.

Usage: ./wc.py <filename>
"""
    # The above is the module's doc-string for documentation
    # Multi-line strings are delimited by triple single/double quotes

# Check if a filename is given in command-line arguments
import sys              # Using 'sys.argv' and 'sys.exit()'
if len(sys.argv) != 2:  # Command-line arguments are kept in a list 'sys.argv'
    print('Usage: ./wc.py <filename>')
    sys.exit(1)         # Return a non-zero value to indicate abnormal termination
    # Note: Python uses indentation instead of {} for body block

# Python's variable has no type. No prior declaration needed.
# Variables are created via the initial assignments.
num_words = num_lines = num_chars = 0  # chain assignment

# Get input file name from 'sys.argv'
# sys.argv[0] is the script name, sys.argv[1] is the filename.
with open(sys.argv[1]) as infile: # 'with-as' closes the file automatically
    for line in infile:           # Process each line (including newline) in a for-loop
        num_lines += 1            # No ++ operator in Python?!
        num_chars += len(line)
        line = line.strip()       # Remove leading and trailing whitespaces
        words = line.split()      # Split into a list using whitespace as delimiter
        num_words += len(words)

# Print results
print('Number of Lines is %d' % num_lines)  # C-like printf()
print('Number of Words is %d' % num_words)
print('Number of Characters is %d' % num_chars)
