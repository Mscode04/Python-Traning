from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def processPayment(self, amount):
        pass

class CreditCardPayment(PaymentMethod):
    def processPayment(self, amount):
        print("Processing credit card payment of ",amount)

class PayPalPayment(PaymentMethod):
    def processPayment(self, amount):
        print("Processing PayPal payment of ",amount)
def process_transaction(payment_method, amount):
    payment_method.processPayment(amount)


credit_card = CreditCardPayment()
paypal = PayPalPayment()

process_transaction(credit_card, 100.50)
process_transaction(paypal, 75.25)



