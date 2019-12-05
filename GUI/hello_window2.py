import tkinter

mainWindow = tkinter.Tk()

mainWindow.title("Hello World")

mainWindow.geometry('1240x860')

label = tkinter.Label(mainWindow, text="Hello Python")
label.pack(side='top')      # Put the label on top

canvas = tkinter.Canvas(mainWindow, relief='raised', borderwidth=2)
# Put canvas on the left side, and expand vertically
canvas.pack(side='left', fill=tkinter.Y)

# Put canvas on top and expand horizontally
#canvas.pack(side='top', fill=tkinter.X)

# Put canvas on top and expand both ways
canvas.pack(side='top', fill=tkinter.BOTH, expand=True)

mainWindow.mainloop()