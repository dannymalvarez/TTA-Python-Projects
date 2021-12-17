''' ABSTRACTION SUBMISSION ASSIGNMENT

Create a class that utilizes the concept of abstraction.


Your class should contain at least one abstract

method and one regular method.  

Create a child class that defines the

implementation of its parents abstract method.

Create an object that utilizes both

the parent and child methods.
 

Add comments throughout your Python explaining your code.


'''


from abc import ABC, abstractmethod #importing abstractmethod from the abc module
class phone(ABC): #creating a parent class as an abstract base class
    def phoneBill(self,amount): #creating a method with parent class inheritance and a new input
        print('Your monthly total is: ',amount)#this function prints a message with the input amount
    @abstractmethod #activating abstractmethod
    def payment(self,amount): #creating an abstract method with parent inheritance and an input amount
        pass #method with no body/content

class CreditCardPayment(phone): #creating a new parents class that inherits from the previous parent class
    def payment(self,amount): #defining the method again without pass this time
        print('Your monthly bill of ' + amount + ' was accepted and processed successfully.')


pay = CreditCardPayment() #instantiating the CCP class which runs the now defined payment method
pay.phoneBill('$50') #instantiating CCP class with phoneBill method
pay.payment('$50') #instantiating CCP class with payment (abstract) method
