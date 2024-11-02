# Section 13, lecture 176

def aver_len(arg):
    total = 0
    wordlist = arg.split(' ')
    print("in aver_len: ")
    for word in wordlist:
        print(word)
        total += len(word)

    print(wordlist)
    print(total)
    print(total/len(wordlist))

def smallest(*arg):
    small = arg[0]
    print(arg)
    for n in arg:
        if n < small:
            small = n
    return small

def backward(*arg):
    print("in backward:")
    print(arg)  # print list of arguments as list
    print("in backward: *arg in reverse")
    for word in arg[::-1]:
        print(word)

backward("this", "is", "forward")

words = "abc edf abcsdf"
aver_len(words)

x = 8/3
y = 8//3
print(x)
print(y)
s = "This is string"
s2 = s + "new string" + str(2)
s3 = "5"
s3 = 5
y = 10 + s3
print(s2)
print(smallest(5, 8, 1, -2, 11))
print(smallest(99, 40))


