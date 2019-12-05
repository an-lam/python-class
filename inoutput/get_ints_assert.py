import sys

def getint(prompt):
    number = int(input(prompt))
    assert -1 < number <= 100, "Number must be between 0 and 100"
    print("number = {}".format(number))
    return number

#first_number = getint("Please enter first number ")

try:
    first_number = getint("Please enter first number ")
except:
    print("We hit error")

second_number = getint("Please enter second number ")

try:
    print("{} divided by {} is {}".format(first_number, second_number, (first_number / second_number)))
except ZeroDivisionError:
    print("You can't divide by zero")
    sys.exit(2)
else:
    print("Division performed successfully")