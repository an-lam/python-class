# Create a program that takes an IP address entered at the keyboard
# and validates that it can be interpreted as a valid IP address.
#
# An IP address consists of 4 numbers, separated from each other with a full stop.
# Each number can have no more than 3 digits.
# Examples are:
# 127.0.0.1
# 192.168.0.1
# 10.0.12.255
# 172.16.57.1
# 255.255.255.0
#
# If the IP address is valid, print the word "ping " followed by the ip address
# otherwise print a suitable error message - the more information you can provide
# in the message the better.
#
# As an optional extra part to the challenge, restrict each number to be between 0 and 255,
# and do not allow 0.0.0.0 as a valid address.
#
# Once you have a working program, here are some suggestions for invalid input to test:
#
# .123.45.678.91
#  123.4567.8.9
#  123.156.289.10123456
# 10.10t.10.10
# 12.9.34.6.12.90
# "" - that is, press enter without typing anything
#
# This challenge is intended to practise for loops, and if/else statements, so although
# it would probably be written for real using regular expressions we don"t want you
# to use them here even if you know what they are.


ipAddress = input("Please enter an IP address: ")

print(ipAddress)

iplist = ipAddress.split(".")
print(iplist)

for i in iplist:
    print(i)
    if int(i) < 0 or int(i) > 255:
        print("invalid segment {}".format(i))

position = 1
segment = 1
number = ""
errorMessage = ""

for digit in ipAddress:
    if digit != ".":
        # we haven"t got a full stop, so we should have a digit
        if digit in "0123456789":
            number += digit
        else:
            errorMessage = "Error in position {} in section {}, invalid character {}".format(position, segment,digit)
            break
    else:
        # we have a full stop, check the length of the number that we"ve built up so far
        if(len(number) == 0) or (len(number) > 3):
            errorMessage = "Error near position {} in section {}, each number must be 1 to 3 digits".format(position,segment)
            break
        if int(number) > 255:
            errorMessage = "Error: near position {}, IP address {} > 255".format(position, number)
            break
        number = ""
        segment += 1
        if segment > 4:
            errorMessage = "Error near position {}, IP address contains more than 4 segments".format(position)
            break
    position += 1
else:
    if(len(number) == 0) or (len(number) > 3):
        errorMessage = "Error near position {} in section {}, each number must be 1 to 3 digits".format(position, segment)
    elif position > 16:
        errorMessage = "Error: IP address can not be more than 15 characters, {} found".format(position)
    elif segment != 4:
        errorMessage = "Error near position {}, IP address contains {} segments, 4 required".format(position, segment)
    else:
        print("ping {}".format(ipAddress))

if errorMessage:
    print(ipAddress)
    print(" " * (position -1) + "^")
    print(errorMessage)