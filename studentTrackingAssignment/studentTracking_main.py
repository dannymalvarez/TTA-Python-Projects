# Python Ver:   3.10.1
#
# Author:       Daniel Alvarez
#
# Purpose:      Tracking student info.

from tkinter import *
from tkinter import messagebox
import tkinter as tk

import studentTracking_func
import studentTracking_gui

class ParentWindow(Frame):
    def __init__(self,master,*args,**kwargs):
        self.master = master
        self.master.minsize(600,400)
        self.master.maxsize(600,400)
        studentTracking_func.center_window(self,600,400)
        self.master.title('Student Tracking')
        self.master.configure('bg=#F0F0F0')

        self.master.protocol('WM_DELETE_WINDOW', lambda: studentTracking_func.ask_quit(self))

        studentTracking_gui.load_gui(self)

        
        menubar = Menu(self.master)
        filemenu = Menu(menubar,tearoff=0)
        filemenu.add_command(label='Exit',underline=1,accelerator='Ctrl+Q',command=lambda: studentTracking_func.ask_quit(self))
        menubar.add_cascade(label='File', underline=0, menu=filemenu)
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_separator()
        helpmenu.add_command(label='How to use this program')
        helpmenu.add_separator()
        helpmenu.add_command(label='About This Student Tracker')
        menubar.add_cascade(label='Help',menu=helpmenu)

        self.master.config(menu=menubar,borderwidth='1')
        












if __name__ == '__main__':
    root=tk.Tk()
    app = ParentWindow(root)
    root.mainloop()
