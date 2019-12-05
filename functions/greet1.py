#!/usr/bin/env python
"""Demonstrates keyword arguments"""

def greet(first, last):
    print('Hello', first, last)

# this is one line comment
greet("Winie", "The Pooh")

greet(last="Robin", first="Christopher")
#greet("An", "Lam")
