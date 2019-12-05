# varargs10.py

# Find the smallest number in the list
# Variable length of argument list
def smallest(*arg):
    #small = -999
    if arg:
        small = arg[0]
        print(arg)
        for n in arg:
            print("n = ", n)
            if n < small:
                small = n

    return small

# Variable length of key-value pair argument list
def print_key_value(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            print("key: {}, value: {}".format(key, value))

#print(smallest())
print(smallest(5, -11))
print(smallest(5, 8, 1, 11, -100))

print_key_value(ip_addr="99.23.7.8", location="San Jose", desc="Windows 10 laptop")
#kv = list(5, 79, 'aa')
#print_key_value
print()
print_key_value(location="San Jose", desc="Windows 10 laptop", ip="1.2.3")


