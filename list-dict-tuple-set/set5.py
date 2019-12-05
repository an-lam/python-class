# set5.py
squares_tuple = (4, 6, 9, 16, 25, 8)
squares = set(squares_tuple)
print(squares)

squares.discard(8)
squares.remove(16)
print(squares)

squares.discard(9) # no error, do nothing because 8 is not in set
squares.remove(100)

print(squares)
# squares.remove(8) # error
if 8 in squares:
    squares.remove(8)
    print(squares)