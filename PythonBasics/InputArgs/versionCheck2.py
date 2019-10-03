import sys

if sys.hexversion >= 0x3000000:
    print("Python 3.x hexversion %s is in use." % hex(sys.hexversion))

else:
    from __future__ import print_function
    print "Current version of python is " + hex(sys.hexversion)
