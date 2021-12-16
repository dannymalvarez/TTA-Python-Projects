
# Creating a parent class named console
class Console:
    controller = True # does it have a controller
    internetAccess = True # does it have access to the internet
    

# creating a child class named Xbox360
class XboxOne(Console):
    manufacturer = 'Microsoft' # who manufactured the console
    nameOfStore = 'Xbox Games Store' # name of system store for game purchases
    traditionalGaming = True # is this a traditional way of gaming, not vr

class Quest(Console):
    virtualReality = True # is it a virtual reality console
    Manufacturer = 'Oculus' # who manufactured this console
    additionalController = True # making an attribute for the helmet/visor
    nameOfStore = 'Oculus Store'
    
