# forloops.py

for i in range(1,5):      # i = 1..4
    print("i is now {}".format(i))

number = "1,675.98"
for i in range(0, len(number)):
    print(number[i])

cleanedNumber = ""        # required
for i in range(0, len(number)):
    if number[i] in '0123456789':
        cleanedNumber = cleanedNumber + number[i]

print(cleanedNumber)
newNumber = int(cleanedNumber)
print("The number is {} ".format(newNumber))

base_file = "write_000"
count = 1
for i in range(0, count):
    file_name = base_file[:-1] + str(i)
    print(file_name)