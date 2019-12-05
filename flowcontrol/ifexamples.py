#!/usr/bin/env # python

age = int(input("Enter your age:"))
#if 66 > age < 15:
if 15 < age < 66:
    print("Have a good day")
else:
    print("Retire")


name = input("Hello! What is your name?\n")

number = 18
print("Well, {0}, I am thinking of a number between 1 and 20.".format(name))

guess = int(input("Take a guess: "))

if guess < number:
   print("Your guess is too low.")

if guess > number:
   print("Your guess is too high.")

if guess == number:
    print("Good job, {0}! You guessed my number!".format(name))
else:
    print("Nope. The number I was thinking of was {0}".format(number))