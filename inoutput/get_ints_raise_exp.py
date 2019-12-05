import sys


def getint(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except EOFError:
            sys.exit(1)
        except ValueError as error:
            print("Exception info: {}".format(error))
            raise OverflowError("My error")   # we raise this exception
        finally:
            print("The finally clause always executes")

try:
    first_number = getint("Please enter first number ")
except OverflowError as err:
    #print("We hit Overflow: {}".format(err))
    print(err)


# second_number = getint("Please enter second number ")
#
# try:
#     print("{} divided by {} is {}".format(first_number, second_number, first_number / second_number))
# except ZeroDivisionError:
#     print("You can't divide by zero")
#     sys.exit(2)
# else:
#     print("Division performed successfully")