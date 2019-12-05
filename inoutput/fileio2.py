# fileio2.py
file_name = "C:\\Users\\lama2\\Pycharmprojects\\inoutput\\sample.txt"

source_file = open(file_name, 'r')
for line in source_file:
    if "Python" in line:
    #if "python" in line.lower():
        print("--- Line with 'python' in it:")
        print(line, end='')

# Close() is required when 'with' statement is not used
source_file.close()

print("\n")
print("-" * 40)

with open(file_name, 'r') as file_handle:
    for line in file_handle:
        if "MAC" in line.upper():
            print("--- Line with 'MAC' in it:")
            print(line, end='')
# Close() is not required when 'with' is used

print("\n")
print("+" * 40)
print("Read one line at a time:")
with open(file_name, 'r') as file_handle:
    line = file_handle.readline()
    while line:
        print(line, end='')
        line = file_handle.readline()

# What's the problem with reading the entire file at once?
with open(file_name, 'r') as file_handle:
    lines = file_handle.readlines()
print("\n\nRead entire file at once using readlines():")
print(lines)

# for line in lines:
#     print(line, end='')
#
print("\n Print file in reversed order:\n")
for line in lines[::-1]:
     print(line, end='')

