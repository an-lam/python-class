# custom_exception1.py

# Example 1:
class CustomValueError(ValueError):
    def __init__(self, arg):
        self.strerror = arg

    def __str__(self):
        return "This comes from CustomValueError:: __str__"

# Example 2:
class CustomException(BaseException):
    pass

def getint(prompt):
    number = int(input(prompt))
    if number < 0 or number > 100:
        raise CustomValueError("Number must be between 0 and 100")
    return number

try:
    number = int(getint("Please enter a number between 0 and 100: "))
except CustomValueError as e:
    print("CustomValueError Exception:", e.strerror)
    print(e)
except CustomException as e:
    print(e)
except:
    print("Exception caught.")
else:
    print("You enter: {}".format(number))
finally:
    print("This statement is always executed.")