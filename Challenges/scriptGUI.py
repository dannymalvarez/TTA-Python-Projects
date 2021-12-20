
import tkinter as tk
from tkinter import *
from tkinter import ttk

class ParentWindow(Frame):
    def __init__ (self,master):
        Frame.__init__ (self)

        self.master = master
        self.master.minsize(600,250)
        self.master.maxsize(600,250)
        self.master.title("Check files")
        self.master.configure(bg="#F0F0F0")

        #configuring the grid
        self.master.columnconfigure(0, weight=1)
        self.master.columnconfigure(1, weight=3)
        
        
        self.varEmpty1 = tk.StringVar()
        self.varEmpty2 = tk.StringVar()
        self.varEmpty1.set('')
        self.varEmpty2.set('')

        self.txtEmpty1 = tk.Entry(self.master,text=self.varEmpty1,font=("Helvetica", 28),fg='lightgray',bg='white')
        self.txtEmpty1.grid(row=0,column=1,padx = (0,20),pady=(30,0),columnspan=2,sticky=tk.E+W)

        self.txtEmpty2 = tk.Entry(self.master,text=self.varEmpty2,font=("Helvetica", 28),fg='lightgray',bg='white')
        self.txtEmpty2.grid(row=1,column=1,padx = (0,20),pady=(15,0),columnspan=2,sticky=tk.E+W)

        self.button1 = tk.Button(self.master, text = "Browse...", width = 10,height=2)
        b1 = self.button1
        b1.grid(row = 0, column = 0,padx=(20,0),pady=(30,0),sticky=tk.W)

        self.button2 = tk.Button( self.master, text = "Browse...", width = 10,height=2)
        b2 = self.button2
        b2.grid(row = 1, column = 0,padx=(20,0),pady=(20,0),sticky=tk.W)
        
        self.button3 = tk.Button( self.master, text = "Check for files...", width = 10, height = 3)
        b3 = self.button3
        b3.grid(row = 2, column = 0,padx=(20,0),pady=(20,0),sticky=tk.W)

        self.button4 = tk.Button( self.master, text = "Close Program", width = 10, height = 3, command = self.close_window)
        b4 = self.button4
        b4.grid(row = 2, column = 2,padx = (0,20),pady=(20,0),sticky=tk.E)

    def close_window(self):
        self.destroy()
        
        '''
        
        
        

     

    #def load_gui (self):
     #   self.txt_fname = tk.Entry(self.master,text='')
      #  self.txt_fname.grid(row=1,column=2,columnspan=8,padx=(30,40),pady=(0,0),sticky=N+E+W)
       

      '''

if __name__ == '__main__':
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()






'''from tkinter import *
from tkinter import messagebox
import tkinter as tk


class ParentWindow(Frame):
    def __init__(self,master,*args,**kwargs):
        Frame.__init__(self,master,*args,**kwargs)

        self.master = master
        self.master.minsize(400,300)
        self.master.maxsize(400,300)

        self.master.title("Check Files")
        self.master.configure(bg="#F0F0F0")
        arg = self.master

        


def load_gui(self):
    self.lbl_fname = tk.Label(self.master,text='First Name:')
    self.lbl_fname.grid(row=0,column=0,padx=(27,0),pady=(10,0),sticky=N+W)


if __name__ == '__main__':
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
'''
