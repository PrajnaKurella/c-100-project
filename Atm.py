class atm(object):
    def __init__(self, pinNumber, cardNumber):
        self.pinNumber = pinNumber
        self.cardNumber = cardNumber

    def pinNumber(self):
        print("enter your pin number: ")

    def cardNumber(self):
        print("enter your card number: ")

    def cashWithDrawal(self):
        print("enter how much you are withdrawing: ")

    def balance(self):
        print("your new balance is: ")

prajna = atm(1234, 3452)
prajna.cardNumber()
prajna.pinNumber()
prajna.cashWithDrawal()
prajna.balance()