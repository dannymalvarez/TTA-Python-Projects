# Python Ver:   3.10.1
#
# Author:       Daniel Alvarez
#
# Purpose:      Tracking student info.

from tkinter import *
from tkinter import messagebox
import tkinter as tk

import studentTracking_func
import studentTracking_main

def load_gui(self):
    self.lbl_fname = tk.Label(self.master,text='First Name:')
    self.lbl_fname.grid(row=0,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    self.lbl_lname = tk.Label(self.master,text='Last Name:')
    self.lbl_lname.grid(row=2,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    self.lbl_phone = tk.Label(self.master,text='Phone Number:')
    self.lbl_phone.grid(row=4,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    self.lbl_email = tk.Label(self.master,text='Email Address:')
    self.lbl_email.grid(row=6,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    self.lbl_course = tk.Label(self.master,text='Current Course:')
    self.lbl_course.grid(row=7,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    self.lbl_info = tk.Label(self.master,text='Information:')
    self.lbl_info.grid(row=0,column=2,padx=(0,0),pady=(10,0),sticky=N+W)
