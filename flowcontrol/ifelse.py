# FlowControl: ifelse.py

name = input("Hello! What is your name?\n")

number = 18
print("Well, {0}, I am thinking of a number between 1 and 20.".format(name))

guess = int(input("Take a guess: "))

if guess < number:
   print("Your guess is too low.")
elif guess > number:
   print("Your guess is too high.")
else:
    print("Good job, {0}! You guessed my number!".format(name))


