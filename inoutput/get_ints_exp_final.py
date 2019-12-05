import sys


def getint(prompt):
    while True:
        try:
            number = int(input(prompt))
            #return number
        # The order of exceptions is important
        #except Exception:   # Catch all, too general
         #   print("Catch all exceptions")
        except ValueError:
            print("Invalid number entered, please try again")
        except EOFError:  # type Ctrl-D hits this exception
            sys.exit(1)
        except Exception:   # Catch all, too general
            print("Catch all exceptions")
        finally:
            print("'finally: always executes.'")
        return number

first_number = getint("Please enter first number ")
second_number = getint("Please enter second number ")

try:
    print("{} divided by {} is {}".format(first_number, second_number, first_number / second_number))
except ZeroDivisionError:
    print("You can't divide by zero")
    sys.exit(2)
else:
    print("'else': Only executes when there is no exception.")

