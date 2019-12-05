# tuples1.py
# Creating tuple

# Are they the same?
car1 = ("Toyota", "Camry", 2.4, 2010)     # tuple
car2 = ["Toyota", "Camry", 2.4, 2010]     # list

emptylist = list()
print(car1)
print(car1[1])
#car1[0] = "Lexus"       # error, why?
car2[0] = "Lexus"
vendor, model, engine, year = car1
#vendor, model, engine, year = car2
print(vendor)
print(model)
print("engine {}".format(car1[2]))
print(year)

# Changing value is not allowed:
#car1[1] = "Corolla"
# Convert tuple into list to allow changes
car1_list = list(car1)
car1_list[1] = "Corolla"
print("list: {}".format(car1_list))

car1 = tuple(car1_list)
print("tuple: {}".format(car1))
# car1[0] = "Honda"      # error. why?

tup = [1, 2, 3]; tup[1] = 4
print(tup)
l = list(tup[2:4]); print(l)

tup = ('a', 'b', 'c', 'd', 'e')
a = ['first', 'second', 'third']; [a1, a2, a3] = a
print(a1, a2, a3)