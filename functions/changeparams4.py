# changeparms.py

def change_parms(first, second):
    print("1. In change_parms: first = {}".format(first))
    first = 100
    print("2. In change_parms: first = {}".format(first))
    # Error if second is a tuple
    second[0] = "surprised"


x = 99
y = [9, 8, 7]

print("Before calling change_parms(): x = {}, y = {}".format(x, y))

change_parms(x, y)
print("After calling change_parms(): x = {}, y = {}".format(x, y))

# don't want changes to your list
new_y = tuple(y)

# Python will complain if change_parms is called
change_parms(x, new_y)
print("x = {}, new_y = {}".format(x, new_y))
