car_list = ["Lexus", "White BMW", "Infiniti"]
car_list.append("Tesla")

for car in car_list:
    print("The car is " + car)

print("orignal list: ", car_list)
car_list.reverse()
print("reverse list: ", car_list)
print("sorted list (reverse):")
print(sorted(car_list, reverse=True))

#print(sorted(car_list))

even = [4, 2]
odd = [1, 3, 5 , 7, 9]

print(even.len)
numbers = even + odd
print(numbers)
numbers_in_order = sorted(numbers)

print("numbers          = {}".format(numbers))
print("numbers_in_order = {}".format(numbers_in_order))

#numbers.sort(reverse=True)

if numbers == numbers_in_order:
    print("1. The lists are equal")
else:
    print("2. The lists are not equal")

if numbers_in_order == sorted(numbers):
    print("3. The lists are equal")
else:
    print("4. The lists are not equal")
