# importrunme.py
# Demonstrate how to import user-defined module
import runme7
from runme7 import runtest2, runtest
#from runme7 import *

print("in importrunme8.py")

runtest()
runtest2()

""" Generic form of import
Assuming PYTHONPATH points to C:\dir0
and dir1 is a subdir of dir0:
import dir1.dir2.module
You must create an init file: __init__.py in dir1 and dir2.
The first time your module is imported, Python will run code 
in this file to initialize your module. It's OK if __init__.py is empty. 
"""