#!/usr/bin/env python
"""Demonstrates defaulted arguments."""

def goToThePark(name, best_friend="Goofey"):
#def goToThePark(name, best_friend):
    print(name + " and " + best_friend)
    print("go to the park play hide-and-seek\n")

goToThePark('Mickey', 'Miney')
goToThePark('Pooh')
