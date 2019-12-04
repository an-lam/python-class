# car1main.py
from car1 import Car

toyota = Car("Toyota", 2005)
print(toyota.make)
print(toyota.year)
print(toyota)

toyota.year = 2017

honda = Car("Honda", 2010)
print("Cars: {}: {}, {}: {}".format(toyota.make, toyota.year, honda.make, honda.year))

print("Cars: {0.make}: {0.year}, {1.make}, {1.year}".format(toyota, honda))

print(toyota.start)
toyota.start_engine()
# same as
#Car.start_engine(toyota)
# There is a bug in start_engine
print(toyota)

print(Car.power_source)
print(toyota.power_source)
print(honda.power_source)

toyota.horse_power = 220  # define new attribute
print("Toyota.horse_power: {} HP".format(toyota.horse_power))
#print(honda.horse_power)  # Error, why?

print("Switch all car power to gas:")
Car.power_source = "gas"
print(Car.power_source)
print(toyota.power_source)
print(honda.power_source)

print("Switch Toyota to hybrid")
toyota.power_source = "hybrid"
print(toyota)

print(honda)

print(Car.__dict__)
print(toyota.__dict__)
print(honda.__dict__)

