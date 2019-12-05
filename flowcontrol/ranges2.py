# ranges2.py

small_decimals = range(0, 10)
print(small_decimals)

print(small_decimals.index(3))

odd = range(1, 1000, 2)
print(odd)

print(odd[85])

sevens = range(7, 1000, 7)
print(sevens)
x = int(input("Please enter a positive number less than one thousand: "))
if x in sevens:
    print("{} is divisible by seven".format(x))
