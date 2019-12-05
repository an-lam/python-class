# set1.py
# Set is unordered.  2 ways to create set:
# 1. use {}
# 2. use set() constructor built-in function
farm_animals = {"sheep", "cow", "hen"} # similar to dictionary?
print(farm_animals)

for animal in farm_animals:
    print(animal)

print("=" * 40)

wild_animals = set(["lion", "tiger", "tiger","panther", "elephant", "hare"])
print(wild_animals)

for animal in wild_animals:
    print(animal)

# Add a member to a set
farm_animals.add("horse")
wild_animals.add("horse")
print(farm_animals)
print(wild_animals)

