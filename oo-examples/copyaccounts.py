# accounts.py

#class Account(object):  Python 2 style: inherits from 'object'
class Account:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
        print("Create account for {}".format(self.name))

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.show_balance()
        else:
            print("Error: amount must be > 0")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Error: without amount must be > 0")

    def show_balance(self):
        print("Balance: ${}".format(self.__balance))


if __name__ == "__main__":
    names = {}
    name = input("Enter your name: ")
    names[0] = Account(name, 500)
    names[1] = Account("Goofey", 99)

    names[0].deposit(110)

    mickey = Account("Mickey", 1000)
    mickey.show_balance()

    mickey.deposit(500)
    mickey.show_balance()

    mickey.withdraw(100)
    mickey.show_balance()
