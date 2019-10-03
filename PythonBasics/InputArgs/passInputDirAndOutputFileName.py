#https://www.guru99.com/python-check-if-file-exists.html
from __future__ import print_function
import sys, platform
import os.path
from os import path

print("__name__ = ",__name__)

print(platform.sys.version_info)




def main():
    outputFile = "globalRBE.xlsx"
    inputDir = os.path.abspath(sys.argv[0]+"/..")
    previousOrParentDir = os.path.abspath(sys.argv[0]+"/../..")
    print("This is the cwd: ", inputDir)
    print("This is the parent/previous directory: ", previousOrParentDir)

    # command line arguments are stored in the form
    # of list in sys.argv
    argumentList = sys.argv
    argnum = len(argumentList)
    print("len(arglist): ",argnum)
    print("arglist: ", argumentList)
    arg0 = sys.argv[0]
    print("arg0: ", arg0)
    if argnum > 1:
        arg1 = sys.argv[1]
        print("arg1: ", arg1)
        #if str(path.exists(arg1)) == True:
        if path.exists(arg1) == True:
            inputDir = arg1
    if argnum > 2:
        arg2 = sys.argv[2]
        print("arg2: ", arg2)
        #if str(path.exists(arg2)) == True:
        outputFile = arg2

    print("Input Dir: ", inputDir)
    print("Output File: ", outputFile)


    print ("file exists:"+str(path.exists('guru99.txt')))
    print ("File exists:" + str(path.exists('career.guru99.txt')))
    print ("directory exists:" + str(path.exists('myDirectory')))

    print ("file versionCheck3.py exists:"+str(path.exists('versionCheck3.py')))
    #print ("File exists:" + str(path.exists('career.guru99.txt')))
    print ("directory exists:" + str(path.exists('/Users/kpadhikari/GitProj/KPAdhikari/PythonStuff/')))
    print ("directory exists:" + str(path.exists('/Users/kpadhikari/GitProj/KPAdhikari/Pytho/')))
    print ("directory exists:" + str(path.exists('/Users/kpadhikari/GitProj/KPAdhikari/PythonStuff/PythonBasics/InputArgs/commandLineArgs1.py')))
    print ("directory exists:" + str(path.exists('/Users/kpadhikari/GitProj/KPAdhikari/PythonStuff/PythonBasics/InputArgs')))
    print ("directory . exists:" + str(path.exists('.')))
    print ("directory .. exists:" + str(path.exists('..')))
    print (". is equivalent to: " +  os.path.abspath(sys.argv[0]+"/.."+"/."))
    print (".. is equivalent to: " +  os.path.abspath(sys.argv[0]+"/.."+"/.."))
    print ("../.. is equivalent to: " +  os.path.abspath(sys.argv[0]+"/.."+"/../.."))

    #if argnum > 1:
    #    print(" The arg for inputDr is: " + os.path.abspath(sys.argv[0]+"/.."+arg1)


if __name__== "__main__":
    main()
