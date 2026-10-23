class Payment:
    
    def process_payment(self, amount):
        print("Procesing payment")

class CreditCard_method(Payment):
    
    def process_payment(self, amount):
        print(f"Paid with CreditCard: {amount} GEL")

class PayPal_method(Payment):

    def process_payment(self, amount):
        print(f"Paid via PayPal: {amount} GEL")

base_payment = Payment()
cc_payment = CreditCard_method()
pp_payment = PayPal_method()

base_payment.process_payment(100)
cc_payment.process_payment(200)
pp_payment.process_payment(300)



    