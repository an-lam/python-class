# whileloop1.py

print("Using for loop: ")
for i in range(5):
     print("i is now {}".format(i))

print("\nUsing while loop")
i = 0
while i < 5:
    print("i is now {}".format(i))
    i += 1

available_exits = ["east", "north east", "south"]
chosen_exit = ""
#chosen_exit = input("Please choose a direction or quit: ")
while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction or quit: ")
    if chosen_exit == "quit":
         print("Game Over")
         break
    else:
        print("Enter again!")

print("The end")