

class vehicle:
    methodOfTransport = 'Undefined'
    fuelType = 'undefined'
    transportPurpose = 'undefined'
    engine = 'undefined'

    def getVehicleInfo(self):
        method = self.methodOfTransport
        

class airplane(vehicle):
    methodOfTransport = 'Air'
    fuelType = 'Aviation Kerosene'
    transportPurpose = 'passenger'
    engine = 'combustion'
    numberOfEngines = 2

    def getVehicleInfo(self):
        method = self.methodOfTransport
        if method = 'Air':
            print('30,000 feet!')
    
class cargoShip(vehicle):
    methodOfTransport = 'Water'
    fuelType = 'Diesel'
    transportPurpose = 'cargo'
    engine = 'combustion'
    numberOfEngines = 4
    
    def getVehicleInfo(self):
        method = self.methodOfTransport
        if method = 'Water':
            print('That\'s no dolphin!')





if __name__ == '__main__':

