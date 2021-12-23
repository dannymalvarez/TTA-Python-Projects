
import tkinter
from tkinter import *
from tkinter import filedialog as fd 
import webbrowser as w
import os
     

go = 'newPage.html' #at the moment this is essentially hardcoded to my local hard drive.
place = '/Users/danielalvarez/Documents/GitHub/TTA-Python-Projects/Challenges/createFreshSite/' #path before file name

placeCheck = os.listdir(place) #this was used to display the path
abPath = os.path.join(place,go) #creating an absolute path for use by combining the path and the file name 
final = 'file://' + abPath #making the path able to open locally on browser



if go in placeCheck: #this if statement checks if 'newPage.html' file exists in the directory
    f = open('newPage.html','r') #opens and reads the file
    f.close() #closes the file
    w.get('chrome').open(final) #opens the file with the absolute path in the specified browser 
        
else: #if file does not exist the following displays an input window for the page content to be altered
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

#This is the entry box where we want the user to input what they would like added to the page
            self.txtsiteInput = Entry(self.master,text=self.siteInput,font=('Helvetica',16),fg='black',bg='lightblue')
            self.txtsiteInput.grid(row=1,column=1,padx=(30,0),pady=(30,0))
#This button submits the info in the text box which when clicked creates the page if it doesnt exist
            self.btnSubmit = Button(self.master,text='Submit', width=6, height=2, command=self.submit)
            self.btnSubmit.grid(row=2,column=1,padx=(0,0),pady=(30,0), sticky=NE)
#this buton closes the display box
            self.btnCancel = Button(self.master,text='Cancel', width=6, height=2, command=self.cancel)
            self.btnCancel.grid(row=2,column=1,padx=(0,110),pady=(30,0), sticky=NE)



        def submit(self):
            info = self.txtsiteInput.get() #setting a variable equal to the input
            f = open('newPage.html','w') #opening a new tab with the hard coded file name that opens a file or creates it 
            f.write('<html><body><h1>'+info+'</h1></body></html>')#inserting the input to the html code for display
            f.close() #closing the file 
            w.get('chrome').open(final) #open the file absolute path in specified browser

        def cancel(self): #closing method
            self.master.destroy()


if __name__ == '__main__':
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()



