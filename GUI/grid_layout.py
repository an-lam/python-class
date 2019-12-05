import tkinter


mainWindow = tkinter.Tk()

mainWindow.title("Grid Layout Example")

mainWindow.geometry('640x480+8+300')

colours = ['red', 'green','orange','white','yellow','blue']

r = 0
for c in colours:
    tkinter.Label(mainWindow, text=c, relief=tkinter.RIDGE,width=15).grid(row=r,column=0)
    # You can type in text in Entry
    tkinter.Entry(mainWindow, bg=c, relief=tkinter.SUNKEN,width=10).grid(row=r,column=1)
    r = r + 1

mainWindow.mainloop()