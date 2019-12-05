#!/usr/bin/env python
# passparams.py

# change(a, c, d, s)
def change(a, b_list, d_dict, s_string):
    a = 22
    b_list[0] = "Python"
    d_dict["apple"] = "a phone"
    s_string = "new string"
    print("in change: ")
    print(a, b_list, d_dict, s_string)

#a = "hello"
a = 99
c = [1, 2]
d = {"apple": "fruit", "salad": "vegetable", 9: "numeric key"}
print(d[9])
s = "abcdef"
print("Before change(): ")
print(a, c, d, s)
change(a, c, d, s)
# a (int) and s (string) are unchanged, but c (list) and d (dictionary) are changed
print("After:")
print(a, c, d, s)

# Update tuple
t = (1, 2, 4)
# t[1] =99
l = list(t)
print(l)
l[1] = 99
t = tuple(l)
print(t)
