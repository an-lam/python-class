
even = set(range(0, 20, 2))
print(sorted(even))
squares_tuple = (4, 6, 9, 16, 25)
squares = set(squares_tuple)
print(sorted(squares))

#print("even plus squares")
#print(sorted(even + squares))
odd = set(range(1, 19, 2))
print("odd minus squares")
print(sorted(odd.difference(squares)))
print(sorted(odd - squares))

print("original odd: " + str(odd))
odd.difference_update(squares)
print("changed odd:  " + str(odd))

# Get the same results
print("squares minus even (same result using either method")
print(squares.difference(even))
print(squares - even)
