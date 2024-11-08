# Recursion10.py

# Calculate the sum of a list using recursion
def my_sum(l):
    if not l:
        return 0
    else:
        return (l[0] + my_sum(l[1:]))

def my_rev(l):
    if not l:
        return 0
    else:
        print(l[0])
        return (my_rev(l[::-1]))


def my_sum2(l):
    total = 0
    for i in l:
        total += i
    return total

def prod(l):
    if not l:
        return 1
    else:
        return(l[0] * prod(l[1:]))


list1 = [2, 3, 4]
# my_rev(list1)
print("prod = ", prod(list1))

list_int = [3, 4, 5, 10]
sum1 = my_sum(list_int)

print("sum = {}".format(sum1))

sum2 = my_sum2(list_int)
print("sum = {}".format(sum2))

total = sum(list_int)
print("total = ", total)
