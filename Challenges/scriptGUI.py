
import tkinter as tk
from tkinter import *
#from tkinter import ttk

class ParentWindow(Frame):
    def __init__ (self,master):
        Frame.__init__ (self)

        self.master = master
        self.master.minsize(500,200)
        self.master.maxsize(500,200)
        self.master.title("Check files")
        self.master.configure(bg="#F0F0F0")

        self.varEmpty1 = StringVar()
        self.varEmpty2 = StringVar()
        self.varEmpty1.set('')
        self.varEmpty2.set('')

        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_rowconfigure(0, weight=1)

        self.txtEmpty1 = Entry(self.master,text=self.varEmpty1,font=("Helvetica", 16),fg='black',bg='white')
        self.txtEmpty1.grid(row=0,column=1)

        self.txtEmpty2 = Entry(self.master,text=self.varEmpty2,font=("Helvetica", 16),fg='black',bg='white')
        self.txtEmpty2.grid(row=1,column=1,columnspan = 3)

        self.button1 = Button(self.master, text = "Browse...", width = 10)
        b1 = self.button1
        b1.grid(row = 0, column = 0)

        self.button2 = Button( self.master, text = "Browse...", width = 10)
        b2 = self.button2
        b2.grid(row = 1, column = 0)
        
        self.button3 = Button( self.master, text = "Check for files...", width = 10, height = 2)
        b3 = self.button3
        b3.grid(row = 2, column = 0)

        self.button4 = Button( self.master, text = "Close Program", width = 10, height = 2, command=self.close_window)
        b4 = self.button4
        b4.grid(row = 2, column = 4)

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
