''' ABSTRACTION SUBMISSION ASSIGNMENT

Create a class that utilizes the concept of abstraction.


Your class should contain at least one abstract method and one regular method.  

Create a child class that defines the implementation of its parents abstract method.

Create an object that utilizes both the parent and child methods.
 

Add comments throughout your Python explaining your code.


'''
from abc import ABC, abstractmethod
class car(ABC):
    def paySlip(self,amount):
        print('Your purchase amount: ',amount)
# this function is telling us to pass in an argument.
# but we won't tell you how or what kind of data that will be
    @abstractmethod
    def payment(self,amount):
        pass

class DebitCardPayment(car):
# Here we've defined how to implement the payment function 
# from its parent paySlip class
    def payment(self,amount):
        print('Your purchase amount of {} exceeded your $100 limit '.format(amount))

obj = DebitCardPayment()
obj.paySlip('$400')
obj.payment('$400')
