
import tkinter
from tkinter import *
from tkinter import filedialog as fd 
import webbrowser as w
import os
     

go = 'newPage.html'
place = '/Users/danielalvarez/Documents/GitHub/TTA-Python-Projects/Challenges/createFreshSite/'

placeCheck = os.listdir(place)
abPath = os.path.join(place,go)
final = 'file://' + abPath



if go in placeCheck:
    f = open('newPage.html','r')
    f.close()
    w.get('chrome').open(final)
        
else:
    class ParentWindow(Frame):
        def __init__ (self,master):
            Frame.__init__ (self)

            self.master = master
            self.master.minsize(600,250)
            self.master.maxsize(600,250)
            self.master.title('What would you like the page to display?')
            self.master.config(bg='lightgray')

            self.siteInput = StringVar()


            self.lblsiteInput = Label(self.master,text='Display Content: ', font=('Helvetica',16),fg='black',bg='lightgray' )
            self.lblsiteInput.grid(row=1,column=0,padx=(30,0),pady=(30,0))

            self.txtsiteInput = Entry(self.master,text=self.siteInput,font=('Helvetica',16),fg='black',bg='lightblue')
            self.txtsiteInput.grid(row=1,column=1,padx=(30,0),pady=(30,0))

            self.btnSubmit = Button(self.master,text='Submit', width=6, height=2, command=self.submit)
            self.btnSubmit.grid(row=2,column=1,padx=(0,0),pady=(30,0), sticky=NE)

            self.btnCancel = Button(self.master,text='Cancel', width=6, height=2, command=self.cancel)
            self.btnCancel.grid(row=2,column=1,padx=(0,110),pady=(30,0), sticky=NE)



        def submit(self):
            info = self.txtsiteInput.get()
            f = open('newPage.html','w')
            f.write('<html><body><h1>'+info+'</h1></body></html>')
            f.close()
            w.get('chrome').open(final)

        def cancel(self):
            self.master.destroy()


if __name__ == '__main__':
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()



