# ranges3.py

# Experiment with different ranges and slices to get a feel for how they work.
# Remember that you can print the range as well as iterating through it to print
# its values, to check that your ranges are what you expected.
# You may also want to include things like.
#
list_4 = range(0, 100, 4)
print("list_4: {0}".format(list_4))
for i in list_4:
    print(i)

items = list_4[::5] # skip 5 elements
print("items: {0}".format(items))
print
for i in items:
    print(i)

# and see if you can work out what will be printed before running the program. If you are unsure, use a
# for loop to print out the values of o to see why p returns what it does.