from tkinter import Tk, Label, Button

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")
        master.geometry('400x200')

        self.label = Label(master, text="Welcome to Python class!")
        self.label.pack()

        # greet() is called when buttion is pressed
        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        # Where is quit() defined?
        self.close_button = Button(master, text="Close", command=master.quit)
        # Use "pack" layout
        self.close_button.pack()

    # Event handler
    def greet(self):
        print("Greetings on console!")

mainWindow = Tk()    # Why not tkinter.Tk() ?
my_gui = MyFirstGUI(mainWindow)
mainWindow.mainloop()