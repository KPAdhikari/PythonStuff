#https://www.geeksforgeeks.org/__name__-special-variable-python/
# File1
  
print('File1 __name__ = {}'.format(__name__)) 
  
if __name__ == "__main__": 
    print("File1 is being run directly")
else: 
    print("File1 is being imported")
