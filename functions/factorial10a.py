# factorial10a.py
# Calculate factorial:
# Example:
#  4! = 4 * 3 * 2 * 1
#  n! = n * (n-1) * (n - 2) *...* 1
def factorial(n):
    print("factorial has been called with n = " + str(n))
    if n == 1:
        return 1
    else:
        res = n * factorial(n-1)
        print("intermediate result for ", n, " * factorial(" ,n-1, "): ",res)
        return res

# Non-recursive version
# Why use non-recursive version?
def iterative_factorial(n):
    result = 1
    for i in range(2,n+1):
        result *= i
        #print("result = " + str(result))

    return result

def fib(n):
    """ F(n) = F(n - 1) + F(n - 2)
        F(1) = 1 """
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

def fibonacci(n):
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        n_minus1 = 1
        n_minus2 = 0
        for f in range(1, n):
            result = n_minus2 + n_minus1
            n_minus2 = n_minus1
            n_minus1 = result
    return result

n = 5
print("{0}! = {1} \n".format(n, factorial(n)))
#print("{0}! = {1} \n".format(n, iterative_factorial(n)))

print("Fibonacci table:")
print("i \t fib(i)  fibonacci")
for i in range(8):
    print(i, "\t", fib(i), "\t\t", fibonacci(i))

