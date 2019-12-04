# accounts2.py
from datetime import datetime


class Account(object):
    """
    Account with transaction history
    """
    # "static method": served as a utility in this case.
    # it has no references to class or instance
    @staticmethod
    def _cur_time():
        return str(datetime.now())

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transactions = []
        print("Create account for {}".format(self.name))

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append((Account._cur_time(), amount))
        else:
            print("Error: amount must be > 0")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append((Account._cur_time(),-amount))
        else:
            print("Error: withdraw amount must be > 0 and less than balance")

    def show_transactions(self):
        for date, amount in self.transactions:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
            print("{} ${:6} on {}".format(tran_type, amount, date) )

    def show_balance(self):
        print("Balance: ${}".format(self.balance))


if __name__ == "__main__":
    mickey = Account("Mickey", 50000000)

    mickey.deposit(500)
    mickey.show_balance()

    mickey.withdraw(10000000)
    mickey.show_balance()

    mickey.show_transactions()
    mickey.show_balance()

    # How do you create more accounts?
    hai = Account("Hai", 10000000)
    hai.show_balance()