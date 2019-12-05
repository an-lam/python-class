# exceptionexp.py
"""
   More details on exceptions:
   https://docs.python.org/3/library/exceptions.html
"""
def factorial(n):
    # n! can also be defined as n * (n-1)!
    """ calculates n! recursively """
    if n <= 1:
        return 1
    else:
        try:
            #print("hello")
           #print(n/0)    # exception will occur
           return n * factorial(n-1)
        except ZeroDivisionError:
           print("Dividing by zero error")
           return n * factorial(n - 1)
        #print(n / 0)  # exception will occur

try:
    print(factorial(1000))
except ZeroDivisionError:
    print("Dividing by zero error")
except (RecursionError, OverflowError):  # multiple exceptions
    print("This program cannot calculate factorials that large")

#Without exception, program crashes
#print(factorial(1000))

"""
try:
    x = 15
    y = x / 0      # exception
except ZeroDivisionError:
    print("Dividing by zero error")
"""

print("Program terminating")

