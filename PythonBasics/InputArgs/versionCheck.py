
#https://stackoverflow.com/questions/9079036/how-do-i-detect-the-python-version-at-runtime
import six

#OK
if six.PY2:
    #x = it.next() # Python 2 syntax
    #print 'six.PY2=' six.PY2
    print "Hello Python2"
else:
    #x = next(it) # Python 3 syntax
    #print('six.PY2=',six.PY2)
    print("Hello Python3")

#Better
#x = six.next(it)
# http://pythonhosted.org/six/
