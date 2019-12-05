# custom_exception1.py

# Example 1:
class CustomValueError(ValueError):
    def __init__(self, arg):
        self.strerror = arg

# Example 2:
class CustomException(BaseException):
    pass

def getint(prompt):
    number = int(input(prompt))
    #if 0 < number > 100:
    if number < 0 or number > 100:
        #raise BaseException
        #raise CustomValueError("Number must be between 0 and 100")
        raise CustomException("CustomException: 0 < number < 100")
    return number

try:
    number = int(getint("Please enter a number between 0 and 100: "))
except CustomValueError as e:
    print("CustomValueError Exception:", e.strerror)
except CustomException as e:
    print(e)
else:   # Execute when no exception
    print("You enter: {}".format(number))
finally:
    print("This statement is always executed.")