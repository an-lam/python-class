
s = "1.2.300.4.99"
items = s.split('.')
print(items)

x = 10 / 2;
print(x)

for i in items:
    if int(i) > 255:
        print("not valid IP: {}".format(i))
    else:
        print(i)

