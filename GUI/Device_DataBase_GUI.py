#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.9
# In conjunction with Tcl version 8.6
#    Sep 29, 2017 12:15:06 PM
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

import Device_DataBase_GUI_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    Device_DataBase_GUI_support.set_Tk_var()
    top = Devices_Database (root)
    Device_DataBase_GUI_support.init(root, top)
    root.mainloop()

w = None
def create_Devices_Database(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    Device_DataBase_GUI_support.set_Tk_var()
    top = Devices_Database (w)
    Device_DataBase_GUI_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Devices_Database():
    global w
    w.destroy()
    w = None


class Devices_Database:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font13 = "-family {Segoe UI} -size 10 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font14 = "-family {Segoe UI} -size 9 -weight bold -slant roman"  \
            " -underline 0 -overstrike 0"
        font15 = "-family {Segoe UI} -size 9 -weight bold -slant "  \
            "italic -underline 0 -overstrike 0"
        font17 = "-family {Segoe UI Emoji} -size 10 -weight bold "  \
            "-slant italic -underline 1 -overstrike 0"
        font18 = "-family {Segoe UI Symbol} -size 11 -weight bold "  \
            "-slant italic -underline 0 -overstrike 0"

        top.geometry("523x371+443+146")
        top.title("Devices Database")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.02, rely=0.03, relheight=0.96, relwidth=0.97)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="4")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#8080ff")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=505)

        vcmd = self.Frame1.register(self.validates)  # define validate cmd
        # Entry widget: displays simple text
        self.ippart1 = Entry(self.Frame1, validate="key", validatecommand=(vcmd, '%P'))  # %P Editable text field
        #self.ippart1 = Entry(self.Frame1)
        self.ippart1.place(relx=0.38, rely=0.14, relheight=0.07, relwidth=0.1)
        self.ippart1.configure(background="#c0c0c0")
        self.ippart1.configure(borderwidth="4")
        self.ippart1.configure(disabledforeground="#a3a3a3")
        self.ippart1.configure(font="TkFixedFont")
        self.ippart1.configure(foreground="#000000")
        self.ippart1.configure(highlightbackground="#d9d9d9")
        self.ippart1.configure(highlightcolor="black")
        self.ippart1.configure(insertbackground="black")
        self.ippart1.configure(selectbackground="#c4c4c4")
        self.ippart1.configure(selectforeground="black")
        self.ippart1.configure(textvariable=Device_DataBase_GUI_support.ipp1)
        self.ippart1.configure(validate="key")

        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.48, rely=0.17, height=10, width=10)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#8080ff")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font14)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''.''')

        self.ippart2 = Entry(self.Frame1, validate="key", validatecommand=(vcmd, '%P'))  # %P Editable text field
        #self.ippart2 = Entry(self.Frame1)
        self.ippart2.place(relx=0.5, rely=0.14, relheight=0.07, relwidth=0.1)
        self.ippart2.configure(background="#c0c0c0")
        self.ippart2.configure(borderwidth="4")
        self.ippart2.configure(disabledforeground="#a3a3a3")
        self.ippart2.configure(font="TkFixedFont")
        self.ippart2.configure(foreground="#000000")
        self.ippart2.configure(highlightbackground="#d9d9d9")
        self.ippart2.configure(highlightcolor="black")
        self.ippart2.configure(insertbackground="black")
        self.ippart2.configure(selectbackground="#c4c4c4")
        self.ippart2.configure(selectforeground="black")
        self.ippart2.configure(textvariable=Device_DataBase_GUI_support.ipp2)
        self.ippart2.configure(validate="key")

        self.Label2 = Label(self.Frame1)
        self.Label2.place(relx=0.59, rely=0.17, height=10, width=10)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#8080ff")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font14)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''.''')

        self.ippart3 = Entry(self.Frame1, validate="key", validatecommand=(vcmd, '%P'))  # %P Editable text field
        #self.ippart3 = Entry(self.Frame1)
        self.ippart3.place(relx=0.61, rely=0.14, relheight=0.07, relwidth=0.1)
        self.ippart3.configure(background="#c0c0c0")
        self.ippart3.configure(borderwidth="4")
        self.ippart3.configure(disabledforeground="#a3a3a3")
        self.ippart3.configure(font="TkFixedFont")
        self.ippart3.configure(foreground="#000000")
        self.ippart3.configure(highlightbackground="#d9d9d9")
        self.ippart3.configure(highlightcolor="black")
        self.ippart3.configure(insertbackground="black")
        self.ippart3.configure(selectbackground="#c4c4c4")
        self.ippart3.configure(selectforeground="black")
        self.ippart3.configure(textvariable=Device_DataBase_GUI_support.ipp3)
        self.ippart3.configure(validate="key")

        self.Label3 = Label(self.Frame1)
        self.Label3.place(relx=0.71, rely=0.17, height=10, width=10)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#8080ff")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font14)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''.''')

        self.ippart4 = Entry(self.Frame1, validate="key", validatecommand=(vcmd, '%P'))  # %P Editable text field
        #self.ippart4 = Entry(self.Frame1)
        self.ippart4.place(relx=0.73, rely=0.14, relheight=0.07, relwidth=0.1)
        self.ippart4.configure(background="#c0c0c0")
        self.ippart4.configure(borderwidth="4")
        self.ippart4.configure(disabledforeground="#a3a3a3")
        self.ippart4.configure(font="TkFixedFont")
        self.ippart4.configure(foreground="#000000")
        self.ippart4.configure(highlightbackground="#d9d9d9")
        self.ippart4.configure(highlightcolor="black")
        self.ippart4.configure(insertbackground="black")
        self.ippart4.configure(selectbackground="#c4c4c4")
        self.ippart4.configure(selectforeground="black")
        self.ippart4.configure(textvariable=Device_DataBase_GUI_support.ipp4)
        self.ippart4.configure(validate="key")

        self.addButton = Button(self.Frame1)
        self.addButton.place(relx=0.04, rely=0.85, height=25, width=65)
        self.addButton.configure(activebackground="#d9d9d9")
        self.addButton.configure(activeforeground="#000000")
        self.addButton.configure(background="#d9d9d9")
        self.addButton.configure(borderwidth="4")
        self.addButton.configure(command=Device_DataBase_GUI_support.callback_add)
        self.addButton.configure(disabledforeground="#a3a3a3")
        self.addButton.configure(font=font15)
        self.addButton.configure(foreground="#000000")
        self.addButton.configure(highlightbackground="#d9d9d9")
        self.addButton.configure(highlightcolor="black")
        self.addButton.configure(pady="0")
        self.addButton.configure(text='''Add New''')

        self.clearButton = Button(self.Frame1)
        self.clearButton.place(relx=0.67, rely=0.85, height=25, width=65)
        self.clearButton.configure(activebackground="#d9d9d9")
        self.clearButton.configure(activeforeground="#000000")
        self.clearButton.configure(background="#d9d9d9")
        self.clearButton.configure(borderwidth="4")
        self.clearButton.configure(command=Device_DataBase_GUI_support.callback_clear)
        self.clearButton.configure(disabledforeground="#a3a3a3")
        self.clearButton.configure(font=font15)
        self.clearButton.configure(foreground="#000000")
        self.clearButton.configure(highlightbackground="#d9d9d9")
        self.clearButton.configure(highlightcolor="black")
        self.clearButton.configure(pady="0")
        self.clearButton.configure(text='''Clear''')

        self.lookupButton = Button(self.Frame1)
        self.lookupButton.place(relx=0.36, rely=0.85, height=25, width=65)
        self.lookupButton.configure(activebackground="#d9d9d9")
        self.lookupButton.configure(activeforeground="#000000")
        self.lookupButton.configure(background="#d9d9d9")
        self.lookupButton.configure(borderwidth="4")
        self.lookupButton.configure(command=Device_DataBase_GUI_support.callback_lookup)
        self.lookupButton.configure(disabledforeground="#a3a3a3")
        self.lookupButton.configure(font=font15)
        self.lookupButton.configure(foreground="#000000")
        self.lookupButton.configure(highlightbackground="#d9d9d9")
        self.lookupButton.configure(highlightcolor="black")
        self.lookupButton.configure(pady="0")
        self.lookupButton.configure(text='''Lookup''')

        self.quitButton = Button(self.Frame1)
        self.quitButton.place(relx=0.83, rely=0.85, height=25, width=65)
        self.quitButton.configure(activebackground="#d9d9d9")
        self.quitButton.configure(activeforeground="#000000")
        self.quitButton.configure(background="#d9d9d9")
        self.quitButton.configure(borderwidth="4")
        self.quitButton.configure(command=Device_DataBase_GUI_support.callback_quit)
        self.quitButton.configure(disabledforeground="#a3a3a3")
        self.quitButton.configure(font=font15)
        self.quitButton.configure(foreground="#000000")
        self.quitButton.configure(highlightbackground="#d9d9d9")
        self.quitButton.configure(highlightcolor="black")
        self.quitButton.configure(pady="0")
        self.quitButton.configure(text='''Quit''')

        self.Label4 = Label(self.Frame1)
        self.Label4.place(relx=0.18, rely=0.03, height=31, width=294)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#8080ff")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font=font13)
        self.Label4.configure(foreground="#800080")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Please enter device's information''')

        self.Message = Message(self.Frame1)
        self.Message.place(relx=0.14, rely=0.68, relheight=0.09, relwidth=0.73)
        self.Message.configure(background="#8080ff")
        self.Message.configure(font=font18)
        self.Message.configure(foreground="#f00000")
        self.Message.configure(highlightbackground="#d9d9d9")
        self.Message.configure(highlightcolor="black")
        self.Message.configure(textvariable=Device_DataBase_GUI_support.msg)
        self.Message.configure(width=370)

        self.Label5 = Label(self.Frame1)
        self.Label5.place(relx=0.09, rely=0.14, height=25, width=100)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#8080ff")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font=font17)
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(justify=LEFT)
        self.Label5.configure(text='''IP Address''')

        self.Label6 = Label(self.Frame1)
        self.Label6.place(relx=0.09, rely=0.28, height=25, width=80)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(background="#8080ff")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(font=font17)
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(highlightbackground="#d9d9d9")
        self.Label6.configure(highlightcolor="black")
        self.Label6.configure(justify=LEFT)
        self.Label6.configure(text='''Location''')

        self.Label7 = Label(self.Frame1)
        self.Label7.place(relx=0.09, rely=0.42, height=25, width=120)
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(activeforeground="black")
        self.Label7.configure(background="#8080ff")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(font=font17)
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(highlightbackground="#d9d9d9")
        self.Label7.configure(highlightcolor="black")
        self.Label7.configure(text='''Serial Number''')

        self.Label8 = Label(self.Frame1)
        self.Label8.place(relx=0.09, rely=0.56, height=25, width=70)
        self.Label8.configure(activebackground="#f9f9f9")
        self.Label8.configure(activeforeground="black")
        self.Label8.configure(background="#8080ff")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(font=font17)
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(highlightbackground="#d9d9d9")
        self.Label8.configure(highlightcolor="black")
        self.Label8.configure(justify=LEFT)
        self.Label8.configure(text='''Model''')

        self.Location = Entry(self.Frame1)
        self.Location.place(relx=0.38, rely=0.28, relheight=0.07, relwidth=0.46)
        self.Location.configure(background="#c0c0c0")
        self.Location.configure(borderwidth="4")
        self.Location.configure(disabledforeground="#a3a3a3")
        self.Location.configure(font="TkFixedFont")
        self.Location.configure(foreground="#000000")
        self.Location.configure(highlightbackground="#d9d9d9")
        self.Location.configure(highlightcolor="black")
        self.Location.configure(insertbackground="black")
        self.Location.configure(selectbackground="#c4c4c4")
        self.Location.configure(selectforeground="black")
        self.Location.configure(textvariable=Device_DataBase_GUI_support.dev_location)

        self.Serial_num = Entry(self.Frame1)
        self.Serial_num.place(relx=0.38, rely=0.42, relheight=0.07
                , relwidth=0.46)
        self.Serial_num.configure(background="#c0c0c0")
        self.Serial_num.configure(borderwidth="4")
        self.Serial_num.configure(disabledforeground="#a3a3a3")
        self.Serial_num.configure(font="TkFixedFont")
        self.Serial_num.configure(foreground="#000000")
        self.Serial_num.configure(highlightbackground="#d9d9d9")
        self.Serial_num.configure(highlightcolor="black")
        self.Serial_num.configure(insertbackground="black")
        self.Serial_num.configure(selectbackground="#c4c4c4")
        self.Serial_num.configure(selectforeground="black")
        self.Serial_num.configure(textvariable=Device_DataBase_GUI_support.dev_serial)

        self.Model_num = Entry(self.Frame1)
        self.Model_num.place(relx=0.38, rely=0.56, relheight=0.07, relwidth=0.46)

        self.Model_num.configure(background="#c0c0c0")
        self.Model_num.configure(borderwidth="4")
        self.Model_num.configure(disabledforeground="#a3a3a3")
        self.Model_num.configure(font="TkFixedFont")
        self.Model_num.configure(foreground="#000000")
        self.Model_num.configure(highlightbackground="#d9d9d9")
        self.Model_num.configure(highlightcolor="black")
        self.Model_num.configure(insertbackground="black")
        self.Model_num.configure(selectbackground="#c4c4c4")
        self.Model_num.configure(selectforeground="black")
        self.Model_num.configure(textvariable=Device_DataBase_GUI_support.dev_model)

        self.deleteButton = Button(self.Frame1)
        self.deleteButton.place(relx=0.2, rely=0.85, height=25, width=65)
        self.deleteButton.configure(activebackground="#d9d9d9")
        self.deleteButton.configure(activeforeground="#000000")
        self.deleteButton.configure(background="#d9d9d9")
        self.deleteButton.configure(borderwidth="4")
        self.deleteButton.configure(command=Device_DataBase_GUI_support.callback_delete)
        self.deleteButton.configure(disabledforeground="#a3a3a3")
        self.deleteButton.configure(font=font15)
        self.deleteButton.configure(foreground="#000000")
        self.deleteButton.configure(highlightbackground="#d9d9d9")
        self.deleteButton.configure(highlightcolor="black")
        self.deleteButton.configure(pady="0")
        self.deleteButton.configure(text='''Delete''')

        self.updateButton = Button(self.Frame1)
        self.updateButton.place(relx=0.51, rely=0.85, height=25, width=65)
        self.updateButton.configure(activebackground="#d9d9d9")
        self.updateButton.configure(activeforeground="#000000")
        self.updateButton.configure(background="#d9d9d9")
        self.updateButton.configure(borderwidth="4")
        self.updateButton.configure(command=Device_DataBase_GUI_support.callback_update)
        self.updateButton.configure(disabledforeground="#a3a3a3")
        self.updateButton.configure(font=font15)
        self.updateButton.configure(foreground="#000000")
        self.updateButton.configure(highlightbackground="#d9d9d9")
        self.updateButton.configure(highlightcolor="black")
        self.updateButton.configure(pady="0")
        self.updateButton.configure(text='''Update''')

    def validates(self, new_text):
        if not new_text: # the field is being cleared
            self.ipaddress = None
            return True

        try:
            print(new_text)
            ipaddress = int(new_text)
            if 1 <= ipaddress <= 255:
                self.ipaddress = ipaddress
                return True
            else:
                return False
        except ValueError:
            return False


if __name__ == '__main__':
    vp_start_gui()



