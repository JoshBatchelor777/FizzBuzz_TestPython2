#   Version: Python 2.7.13
#
#   Author: Josh Batchelor, 12/7/2017
#
#   Purpose: To take logic from my
#   C# Fizz Buzz test, and apply it to 
#   Python.
#

print("Welcome to Fizz Buzz in Python 2!")

for i in range(1,21,1):
    if i%3 == 0 and i%5 == 0:
        print("Fizz Buzz ({})".format(i))
        
    if i%3 != 0 and i%5 != 0:
        print (i)
    elif i%3 == 0 and i !=15:
        print("Fizz ({})".format(i))
    elif i%5 == 0and i != 15:
        print("Buzz ({})".format(i))


