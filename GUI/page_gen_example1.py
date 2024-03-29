#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.9
# In conjunction with Tcl version 8.6
#    Sep 10, 2017 12:48:10 AM
import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import Page-generated-sample1_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = An_Lam_sample (root)
    Page-generated-sample1_support.init(root, top)
    root.mainloop()

w = None
def create_An_Lam_sample(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = An_Lam_sample (w)
    Page-generated-sample1_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_An_Lam_sample():
    global w
    w.destroy()
    w = None


class An_Lam_sample:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'

        top.geometry("600x450+417+210")
        top.title("An Lam sample")
        top.configure(background="#d9d9d9")



        self.Button_2 = Button(top)
        self.Button_2.place(relx=0.13, rely=0.76, height=24, width=27)
        self.Button_2.configure(activebackground="#d9d9d9")
        self.Button_2.configure(activeforeground="#000000")
        self.Button_2.configure(background="#d9d9d9")
        self.Button_2.configure(disabledforeground="#a3a3a3")
        self.Button_2.configure(foreground="#000000")
        self.Button_2.configure(highlightbackground="#d9d9d9")
        self.Button_2.configure(highlightcolor="black")
        self.Button_2.configure(pady="0")
        self.Button_2.configure(text='''OK''')

        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.13, rely=0.09, relheight=0.61, relwidth=0.68)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(width=405)

        self.Entry1 = Entry(self.Frame1)
        self.Entry1.place(relx=0.35, rely=0.11, relheight=0.07, relwidth=0.4)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.2, rely=0.11, height=21, width=38)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Name''')






if __name__ == '__main__':
    vp_start_gui()