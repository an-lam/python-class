# assert1.py

def getint(prompt):
    number = int(input(prompt))
    assert 0<= number < 100, "Number must be between 0 and 100"
    print("number = {}".format(number))
    return number

#first_number = getint("Please enter a number between 0 and 100: ")

try:
    first_number = getint("Please enter a number between 0 and 100: ")
except:
    print("We hit error")

print("No error if we get here.")
