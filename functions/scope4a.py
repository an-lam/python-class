#!/usr/bin/env python
# scope4a.py
"""Global/module-level identifier behavior."""

x = 99

def func1():
    global x
    x += 10
    print("in func1 (global x): x = {}".format(x))

def func2():
    x = 200
    print("in func2 (local x): x = {}".format(x))

def func3():
    x = 100
    print("1. in func3: x = {}".format(x))
    x += 100
    print("2. in func3: x = {}".format(x))
    y = 2
    print("in func 3 locals : {}".format(locals()))
    print("in func 3 globals : {}".format(globals()))

func1()
func2()
func3()

print("\n In main: x = {}".format(x))

print(locals())
print(globals())