even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

# numbers has 2 lists
numbers = [even, odd]

print("numbers: {}".format(numbers))

for number_set in numbers:
    print(number_set)

    print("value in number_set:")
    for value in number_set:
        print(value)
    print("\n")

list_1 = []
list_2 = list()
list_3 = list_1      # reference the same object
print("List 1: {}".format(list_1))
print("List 2: {}".format(list_2))
# Test object identity
if list_1 is list_3:
    print("1. The lists are equal because they are the same object")
else:
    print("2. The lists are not equal")

list_3.append(5)
print("new list_3 = {}".format(list_3))

# Test value equivalence
if list_1 == list_2:
    print("3. The lists are equal because both are empty")
else:
    print("4. The lists are not equal: {} != {} ".format(list_1, list_2))

# Test object identity again
list_1 = [1, 2, 3]
list_3 = list_1       # construct a new list
print(list_1)
print(list_3)
if list_1 is list_3:
# if list_1 == list_3:
    print("5. The lists are equal")
else:
    print("6. The lists are not equal because they are not the same object")
    print(list_3)