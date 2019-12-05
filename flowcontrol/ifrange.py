#!/usr/bin/env # python


age = int(input("How old are you?"))
# if (age >= 16) and (age <= 65)
if 66 > age > 15:
   print("Have a good work day.")
   print()

if not(age < 21):
    print("You are old enough to drink")
else:
    print("Please come back in {0} years".format(21 - age))