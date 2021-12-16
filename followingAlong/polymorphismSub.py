

class vehicle: # creating a parent class
    methodOfTransport = 'Undefined' #creating various attributes
    fuelType = 'undefined'
    transportPurpose = 'undefined'
    engine = 'undefined'

    def getVehicleInfo(self): #created a method that sets method equal to the value of methodOfTransport
        method = self.methodOfTransport
        

class airplane(vehicle): #creating first child class
    methodOfTransport = 'Air'
    fuelType = 'Aviation Kerosene'
    transportPurpose = 'passenger'
    engine = 'combustion'
    numberOfEngines = 2
    crewSize = 2 # changed parent attribute values and added a new one

    def getVehicleInfo(self): # used polymorphism to add an if statement
        method = self.methodOfTransport
        if method == 'Air':
            print('30,000 feet!') #prints out a fun message if method === 'Air'
    
class cargoShip(vehicle): # creating second child class
    methodOfTransport = 'Water'
    fuelType = 'Diesel'
    transportPurpose = 'cargo'
    engine = 'combustion'
    numberOfEngines = 4
    crewSize = 14 # changed parent attribute values and added a new one
    
    def getVehicleInfo(self):
        method = self.methodOfTransport
        if method == 'Water':
            print('That\'s no dolphin!') #prints out a not-so-fun message if method === 'Water'





if __name__ == '__main__':
    print(cargoShip().getVehicleInfo())
    print(airplane().getVehicleInfo())
    
