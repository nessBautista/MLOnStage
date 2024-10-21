from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paying {amount} using credit card"
    
class PayPalPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paying {amount} using PayPal"
    
class BitcoinPayment(PaymentMethod):
        def pay(self, amount):
             return f"Paying {amount} using Bitcoin"


### Context 
class ShoppingCart:
    def __init__(self, paymentMethod: PaymentMethod):
        self.paymentMethod = paymentMethod

    def checkout(self, amount):
        return self.paymentMethod.pay(amount)
    
if __name__ == "__main__":
    cart = ShoppingCart(CreditCardPayment())
    print(cart.checkout(100))

    cart = ShoppingCart(PayPalPayment())
    print(cart.checkout(100))

    cart = ShoppingCart(BitcoinPayment())
    print(cart.checkout(100))
