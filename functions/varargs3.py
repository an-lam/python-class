# varargs3.py
def print_hello():
    print("Hello world!")
    # return 1

# Parameter: text
# variable arg must be passed in before other args
def centre_text(*args, sep=' ', end='\n', file=None):
    # for arg in args:
    #    print(arg)
    text = ""
    for arg in args:
        print(arg)
        text += str(arg) + sep
        #text += arg + sep
        left_margin = (80 - len(text)) // 2  # // means integer division
        print("-" * left_margin, text, end=end, file=file)

#print_hello()
#print(print_hello())

# call the function with different arguments
centre_text("1")
centre_text("apple, orange", "banana", sep="*")
centre_text("orange", "lime", 3, 4, "grape", "pear")

# print using separator and end
# NOTE: Make sure your Python version > 3.6
# File->Setting->Project Functions->Project Interpreter = Python 3.6 path
print(1, 2, 3, 4, sep=':', end='\n\n')
print(4, 5, "abcd", 6, 7, sep=';')