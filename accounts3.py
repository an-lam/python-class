# accounts3.py
from datetime import datetime


class Account:
    """
    Account with __balance (prefix with 2 underscores) to prevent accidental access
    """

    @staticmethod
    def _cur_time():
        return str(datetime.now())

    def __init__(self, name, balance):
        self.name = name
        # Change balance to __balance to ask Python to hide it by name mangling
        self.__balance = balance
        self.transactions = []
        print("Create account for {}".format(self.name))

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.transactions.append((Account._cur_time(), amount))
        else:
            print("Error: amount must be > 0")

    def withdraw(self, amount):
        if 0< amount <= self.__balance:
            self.__balance -= amount
            self.transactions.append((Account._cur_time(),-amount))
        else:
            print("Error: without amount must be > 0")

    def show_transactions(self):
        for date, amount in self.transactions:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
            print("{} ${:6} on {}".format(tran_type, amount, date) )

    def show_balance(self):
        print("Balance: ${}".format(self.__balance))


if __name__ == "__main__":
    mickey = Account("Mickey", 1000)

    mickey.deposit(500)
    mickey.show_balance()

    mickey.withdraw(100)
    mickey.show_balance()

    # Not a good idea, won't work
    # because Python uses name mangling to hide the actual __balance variable
    mickey.__balance = 999999

    #mickey.show_transactions()
    #mickey.show_balance()
    print(mickey.__balance)
    # Show what the variables are
    print(mickey.__dict__)