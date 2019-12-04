# car1main.py
from car1 import Car

toyota = Car("Toyota", 2005)
print(toyota.make)
print(toyota.year)
print(toyota)

lexus = Car("Lexus")
print(lexus)

toyota.year = 2017
lexus.year = 2019
print(lexus)

honda = Car("Honda", 2010)
# 2 ways to print data attributes
print("Cars: {}: {}, {}: {}".format(toyota.make, toyota.year, honda.make, honda.year))
print("Cars: {0.make}: {0.year}, {1.make}, {1.year}".format(toyota, honda))

print(toyota.start)
toyota.start_engine()
toyota.start = True
print(toyota)
# same as
Car.start_engine(toyota)
# There is a bug in start_engine ?
print(toyota)

print(Car.power_source)
print(toyota.power_source)
print(honda.power_source)

toyota.horse_power = 220  # define new attribute
print("Toyota.horse_power: {} HP".format(toyota.horse_power))
Car.horse_power = 110    # define new class attribute
print(honda.horse_power)  # Error (if above line is commented out), why?
print(toyota.horse_power)

print("Switch all car power to gas:")
Car.power_source = "gas"
print(Car.power_source)
print(toyota.power_source)
print(honda.power_source)
print(honda.make)

print("Switch Toyota to hybrid")
toyota.power_source = "hybrid"
print(toyota)

# honda power_source should remain "gas"
print(honda)

# Print all attributes belonging to objects
print(Car.__doc__)
print(Car.__dict__)
print(toyota.__dict__)
print(honda.__dict__)

