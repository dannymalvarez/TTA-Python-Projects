class computer:
    screen = True
    brand = 'Undefined'
    keyboard = 'Undefined'
    cpu = True

    def print(self):
        print(self.screen,self.cpu)

class laptop(computer):
    keyboard = 'Internal'
    brand = 'Apple'

if __name__ == '__main__':

    
    print(laptop().print())
