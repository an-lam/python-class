import random
from tkinter import Tk, Label, Button, Entry, StringVar, DISABLED, NORMAL, END, W, E

"""
Homework:  Add a "Quit" button to quit the game
"""

class GuessingGame:
    def __init__(self, master):
        self.master = master
        master.title("Guessing Game")
        master.geometry('500x300')

        self.secret_number = random.randint(1, 100)
        self.guess = None
        self.num_guesses = 0

        self.message = "Guess a number from 1 to 100"
        self.label_text = StringVar()
        self.label_text.set(self.message)
        self.label = Label(master, textvariable=self.label_text)

        # define validate cmd to validate input
        vcmd = master.register(self.validate)
        # Entry widget: displays simple text
        # '%P': indicates the text area is editable field, the validate() function
        # is called when key is pressed (validate="key")
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))

        # Call guess_number() if the "Guess" is pressed
        self.guess_button = Button(master, text="Guess", command=self.guess_number)

        # Call reset() if the "Play again" button is pressed
        self.reset_button = Button(master, text="Play again", command=self.reset, state=DISABLED)

        # Using grid layout: specifying row, column position
        self.label.grid(row=0, column=0, columnspan=2, sticky=W+E)
        self.entry.grid(row=1, column=0, columnspan=2, sticky=W+E)
        self.guess_button.grid(row=2, column=0)
        self.reset_button.grid(row=2, column=1)

    """
    This function takes text input from user.
    :parameter new_text: the text input from user
    :return:
         True - the input text is valid
         Fale - the input text is not valid
    """
    def validate(self, new_text):
        if not new_text:   # the field is being cleared
            self.guess = None
            return True

        try:
            # print to console below
            print(new_text)
            guess = int(new_text)  # convert input text into int
            if 1 <= guess <= 100:
                self.guess = guess
                return True
            else:
                # conversion fails
                return False
        except ValueError:
            return False

    def guess_number(self):
        self.num_guesses += 1

        if self.guess is None:
            self.message = "Guess a number from 1 to 100"

        elif self.guess == self.secret_number:
            suffix = '' if self.num_guesses == 1 else 'es'
            self.message = "Congratulations! You guessed the number after %d guess%s." % (self.num_guesses, suffix)
            self.guess_button.configure(state=DISABLED)
            self.reset_button.configure(state=NORMAL)

        elif self.guess < self.secret_number:
            self.message = "Too low! Guess again!"
        else:
            self.message = "Too high! Guess again!"

        self.label_text.set(self.message)

    def reset(self):
        self.entry.delete(0, END)
        self.secret_number = random.randint(1, 100)
        self.guess = 0
        self.num_guesses = 0

        self.message = "Guess a number from 1 to 100"
        self.label_text.set(self.message)

        self.guess_button.configure(state=NORMAL)
        self.reset_button.configure(state=DISABLED)

root = Tk()
my_gui = GuessingGame(root)
root.mainloop()