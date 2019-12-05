# fileappend.py
#
# Write a program to append the times tables to
# cities.txt. We want the tables from 2 to 9
#
# The first column of numbers should be right justified. As an example,
# the 2 times table should look like this:
#   1 times 2 is 2
#   2 times 2 is 4
#   3 times 2 is 6
#   4 times 2 is 8
#   5 times 2 is 10
#   6 times 2 is 12
#   7 times 2 is 14
#   8 times 2 is 16
#   9 times 2 is 18
#  --------------------
with open("cities.txt", 'a') as tables:
    for i in range(2, 10):
        for j in range(1, 10):
            print("{1}    times    {0} is {2}".format(i, j, i * j), file=tables)
        print("-" * 20, file=tables)