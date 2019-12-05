import tkinter as tk
import random

mainwindow = tk.Tk()
# width x height + x_offset + y_offset:
mainwindow.geometry("300x300+30+30")
mainwindow.title("Place Layout Example")

languages = ['Python', 'Perl', 'C++', 'Java', 'Tcl/Tk']
labels = range(5)
for i in range(5):
    ct = [random.randrange(256) for x in range(3)]
    brightness = int(round(0.299 * ct[0] + 0.587 * ct[1] + 0.114 * ct[2]))
    ct_hex = "%02x%02x%02x" % tuple(ct)
    bg_colour = '#' + "".join(ct_hex)
    label1 = tk.Label(mainwindow,
                 text=languages[i],
                 fg='White' if brightness < 120 else 'Black',
                 bg=bg_colour)
    label1.place(x=20, y=30 + i * 30, width=120, height=25)

mainwindow.mainloop()