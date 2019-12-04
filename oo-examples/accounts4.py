# accounts4.py
from datetime import datetime


# Something is wrong with numeric values ?
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
        self.transactions = []   # empty list
        print("Create account for {}".format(self.name))

    def deposit(self, amount):
        if amount > 0:
            amount /= 1.0
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
        print("Balance: ${:3}".format(self.__balance))


if __name__ == "__main__":
    mickey = Account("Mickey", 10.10)
    mickey.show_balance()

    mickey.deposit(0.10)
    mickey.deposit(0.10)

    mickey.withdraw(0.30)
    # mickey.show_transactions()

    mickey.show_balance()

"""
What's wrong with balance?
Create account for Mickey
Balance: $10.1
deposited $   0.1 on 2018-03-09 23:23:44.413424
deposited $   0.1 on 2018-03-09 23:23:44.413424
withdrawn $  -0.3 on 2018-03-09 23:23:44.413424
Balance: $9.999999999999998
"""
