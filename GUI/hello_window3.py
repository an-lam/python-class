import tkinter

mainWindow = tkinter.Tk()

mainWindow.title("Hello World")

mainWindow.geometry('640x480+8+300')

label = tkinter.Label(mainWindow, text="Hello Python")
label.pack(side='top')      # Put the label on top

canvas = tkinter.Canvas(mainWindow, relief='raised', borderwidth=2)
# Put canvas on the left side, and expand vertically
#canvas.pack(side='left', fill=tkinter.Y)
canvas.pack(side='left')

button1 = tkinter.Button(mainWindow, text="OK")
button2 = tkinter.Button(mainWindow, text="Save")
button3 = tkinter.Button(mainWindow, text="cancel")

button1.pack(side='top')
button2.pack(side='top')
button3.pack(side='top')

#button1.pack(side='left', anchor='n')
#button2.pack(side='left', anchor='s')
#button3.pack(side='left', anchor='e')



mainWindow.mainloop()