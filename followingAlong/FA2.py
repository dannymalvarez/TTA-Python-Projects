class technology:
    internetAccess = True
    screenSize = 'Undefined'
    manufacturer = 'Undefined'
    physicalKeyboard = 'Undefined'
    screen = True

mfg = technology()
print(mfg.manufacturer)

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = Person('John',14)

print(p1.name)
print(p1.age)

class PersonB:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def myfunc(self):
        print('Hello my name is ' + self.name)

p2 = PersonB('John', 14)
p2.myfunc()
