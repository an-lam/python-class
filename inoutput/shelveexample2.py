import shelve

# shelve is open as both 'read' and 'write'
# A database is created.

# with shelve.open('ShelfTest') as fruit:
fruit = shelve.open('ShelfTest')
# fruit['orange'] = "a sweet, orange, citrus fruit"
# fruit['apple'] = "good for making cider"
# fruit['lemon'] = "a sour, yellow citrus fruit"
# fruit['grape'] = "a small, sweet fruit growing in bunches"
# fruit['lime'] = "a sour, green citrus fruit"

# Access like a dictionary
# make a new entry
fruit["durian"] = "tastes good."
print(fruit["durian"])

print("keys: ")
for keys in fruit:
    print(keys)

print("-" *10)
for k in fruit:
    print(fruit[k])

# Assume the database was created by running shelveexample.py
# before running this program.
while True:
    fruit_key = input("Please enter a fruit: ")
    if fruit_key in ["quit", "q", "Q" ]:
        break

    #desc = fruit.get(fruit_key)
    desc = fruit.get(fruit_key, "We don't have a " + fruit_key)
    print(desc)

# close shelve manually if you don't use "with" statement
fruit.close()
