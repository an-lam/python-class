# fileio1.py

# Read text file
myfile = open("sample2.txt",'r')
#myfile = open("C:\\Users\\lama2\\Pycharmprojects\\inoutput\\fileio1.py", 'r')
for line in myfile:
    #print(line)
    print(line.rstrip('\n'))

myfile.close()

