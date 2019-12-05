# set6.py
even = set(range(0, 40, 2))
even.add(100)
print(even)
squares_tuple = (4, 6, 16)
squares = set(squares_tuple)
print(squares)

if squares.issubset(even):
    print("Squares is a subset of even")

if even.issuperset(squares):
    print("Even is a superset of squares")

even2 = frozenset(range(0, 50, 2))
even2.add(52)   # error, whhy?