#!/usr/bin/env python
"""Function with many arguments and many return values."""

def analyze(one, other):
    total = sum((one, other)) # sum demands a sequence
    average = total/2.0      # min and max are flexible
    return min(one, other), max(one, other), total, average

def myPrint(min_number, max_number, total, average):
    print("min_number=", min_number)
    print("max_number=", max_number)
    print("total=", total,)
    print("average=", average)
    print

def main():
    min_number, max_number, total, average = analyze(1, 8)
    myPrint(min_number, max_number, total, average)

    answer = analyze(100, 50)
    print(answer)
    min_number, max_number, total, average = answer
    myPrint(min_number, max_number, total, average)

main()
