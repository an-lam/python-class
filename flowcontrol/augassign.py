number = "9,223,372,807"
cleanedNumber = ''

for i in range(0, len(number)):
    if number[i] in '0123456789':
        cleanedNumber += number[i]

newNumber = int(cleanedNumber)
print("The number is {} ".format(newNumber))

x = 23
x += 1           # Note i++ is not valid syntax
print(" x += 1 -> {}".format(x))

x -= 4
print(" x -= 4 -> {}".format(x))

x *= 5
print(" x *= 5 -> {}".format(x))

x /= 4
print(" x /=4 -> {}".format(x))

x **=2
print(" x **= 2 -> {}".format(x))

x %= 60
print(" x %= 60 -> {}".format(x))

x, y, z = 5, 10, 15
print("x = {0}, y = {1}, z = {2}".format(x, y, z))

x, y = y, x
print("x = {0}, y = {1}".format(x, y))

a = b = c = 12
print("c = " + str(c))
#print("c = " + c)    # What's wrong with this statement?

greeting = "Good "
greeting += "morning "
print(greeting)

greeting *= 3
print(greeting)

a, b = 1, (2, 3)
print("a = {}, b = {}".format(a, b))
