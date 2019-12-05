# truefalse.py
# Similar to C:
# anything that is not zero is true
x = "false"
if x:
    print("x = 'false', x is true")
else:
    print("x is false")

x = int(input("Please enter a number or hit 'enter' key:"))

if x:
    print("True: You entered '{}'".format(x))
else:
    print("False: You enter '{}'".format(x))
