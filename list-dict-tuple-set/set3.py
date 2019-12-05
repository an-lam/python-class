even = set(range(0, 10, 2))
print("1. even = {}".format(even))
squares_tuple = (6, 4, 9, 16)
squares = set(squares_tuple)
print("2. squares = {}".format(squares))

print("3. even union with squares")
print(even.union(squares))
print("4. len = {}, even (unchanged) = {}".format(len(even), even))
print(len(even.union(squares)))

print("5. squares union with even using union and '|' ")
print(squares.union(even))
print(squares | even)

print(squares)   # Unchanged

print("-" * 40)

print("6. even intersection with squares using intersection and '&'")
print(even.intersection(squares))
print(even)
print(even & squares)

print("7. squares intersection with even")
print(squares.intersection(even))
print(squares & even)

