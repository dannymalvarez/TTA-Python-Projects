'''
Create a class that uses encapsulation. Requirements include:


This class should make use of a private attribute or function.

This class should make use of a protected attribute or function.

Create an object that makes use of protected and private.

Add comments throughout your Python explaining your code.

Upload your code to GitHub and submit your link below.  
'''



    
class protect: #creating a class
    def __init__(self):
        self._number = 5 #creating protected variable
        

    def __init__(self):
        self.__oldYear = 1900 # creating private variable

    def getYear(self):
        print(self.__oldYear) # this prints the original private var

    def setYear(self,currentYear):
        self.__oldYear = currentYear # this sets original private var to new value


newNum = protect() # set newNum variable = to protect(ed) class
newNum._number = 20 #setting protected variable to new value
print(newNum._number) # printing new value

year = protect() # set year variable = to protect(ed) class
year.getYear() # calling child class which prints it's year variable
year.setYear(2021) # setting old year variable to current year
year.getYear() #calling child class which now prints updated current year 
