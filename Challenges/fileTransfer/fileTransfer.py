import shutil
import os
import time
from datetime import datetime
import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd

class ParentWindow(Frame): #gui
    
    def __init__ (self,master):
        Frame.__init__(self)
    
        self.master = master
        self.master.minsize(600,250)#setting a size for it to fit and look nice
        self.master.maxsize(600,250)
        self.master.title("Check files") #title of the gui window
        self.master.configure(bg="#F0F0F0") #gui color for background

        #configuring the grid
        self.master.columnconfigure(0, weight=1)
        self.master.columnconfigure(1, weight=3) #this was the only way I could get the length of the columnspan columns to work right
  
        self.varEmpty1 = tk.StringVar() #setting variables to be strings using tkinter
        self.varEmpty2 = tk.StringVar()
        self.varEmpty3 = tk.StringVar()
        
# setting empty variables to tkinter entry methods with positioning, font, font size, and other info
        self.txtEmpty1 = tk.Entry(self.master,text=self.varEmpty1,font=("Helvetica", 25),fg='black',bg='white')
        self.txtEmpty1.grid(row=0,column=1,padx = (0,20),pady=(30,0),columnspan=2,sticky=tk.E+W)

        self.txtEmpty2 = tk.Entry(self.master,text=self.varEmpty2,font=("Helvetica", 25),fg='black',bg='white')
        self.txtEmpty2.grid(row=1,column=1,padx = (0,20),pady=(15,0),columnspan=2,sticky=tk.E+W)

        self.txtEmpty3 = tk.Entry(self.master,text=self.varEmpty3,font=("Helvetica", 25),fg='black',bg='white')
        self.txtEmpty3.grid(row=2,column=1,padx = (0,20),pady=(15,0),sticky=tk.E+W)
# creating button that use commands from below
        self.button1 = tk.Button(self.master, text = "Source Folder", width = 10,height=2,command=self.source)
        b1 = self.button1
        b1.grid(row = 0, column = 0,padx=(20,10),pady=(30,0),sticky=tk.W)

        self.button2 = tk.Button( self.master, text = "Destination Folder", width = 10,height=2,command=self.destination)
        b2 = self.button2
        b2.grid(row = 1, column = 0,padx=(20,0),pady=(20,0),sticky=tk.W)
    
        self.button3 = tk.Button(self.master, text = "Check for files", width = 10, height = 3,command=self.check)
        b3 = self.button3
        b3.grid(row = 2, column = 0,padx=(20,0),pady=(20,0),sticky=tk.W)

        self.button4 = tk.Button(self.master, text = "Close Program", width = 10, height = 3,command=self.close)
        b4 = self.button4
        b4.grid(row = 2, column = 2,padx = (0,20),pady=(20,0),sticky=tk.E)

#set where the source of the files are
    def source(self):
        sourcePath = fd.askdirectory()
        self.varEmpty1.set(sourcePath)


#set the destination path to folder of choice
        
    def destination(self):
        destinationPath = fd.askdirectory()
        self.varEmpty2.set(destinationPath)


# method to check using comparisons accurate to the hour between files to determine which should be moved
    def check(self):
        now = datetime.now()
        currentHour = now.strftime('%I')
        currentDay = now.strftime('%d')
        currentMonth = now.strftime('%m')
        currentYear = now.strftime('%Y')

        source = self.varEmpty1.get()
        files = os.listdir(source)
        destination = self.varEmpty2.get()
        print(files)# print files in the source path, this helped me figure out what was wrong which was that there was a .DS_Store file
        print(destination) #print destination path 
        print(source) #print source path

        for i in files:
            modTime = (time.ctime(os.path.getmtime(source+"/"+i)))
            modTimeObj = datetime.strptime(modTime, '%a %b %d %H:%M:%S %Y')
            modTimeHour = modTimeObj.strftime("%I")
            modTimeDay = modTimeObj.strftime("%d")
            modTimeMonth = modTimeObj.strftime("%m")
            modTimeYear = modTimeObj.strftime("%Y")

            if currentYear == modTimeYear and currentMonth == modTimeMonth and currentDay == modTimeDay and currentHour and modTimeHour:
                self.varEmpty3.set('Files transferred.') #making use of the third entry box by having it display some text based on success or failure of method.
                shutil.move(source+"/"+i,destination)
            else:
                self.varEmpty3.set('There were no files to transfer') 


    def close(self):
        self.master.destroy()
        

if __name__ == '__main__':
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
