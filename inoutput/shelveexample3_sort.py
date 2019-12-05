import shelve

# shelve is open as both 'read' and 'write'
# A database is created.

# with shelve.open('ShelfTest') as sfruit:
fruit = shelve.open('ShelfTest')
# fruit['orange'] = "a sweet, orange, citrus fruit"
# fruit['apple'] = "good for making cider"
# fruit['lemon'] = "a sour, yellow citrus fruit"
# fruit['grape'] = "a small, sweet fruit growing in bunches"
# fruit['lime'] = "a sour, green citrus fruit"

for f in fruit:
    print(f + " - " + fruit[f])

for i in range(0, 2):
    print("=" * 40)

ordered_keys = list(fruit.keys())
print("keys are not sorted yet: {}\n".format(ordered_keys))
# ordered_keys are sorted in memory after calling ordered_keys.sort()
ordered_keys.sort()

print("Fruit in sorted key order:")
for f in ordered_keys:
    print(f + " - " + fruit[f])

# Question:
# Is the external DB sorted by this code?

# close shelve manually
fruit.close()

