# accounts5.py
from datetime import datetime

# Fix rounding errors
class Account:
    """
    Account with __balance (prefix with 2 underscores) to prevent accidental access
    """

    def __init__(self, name, balance: int = 0):
        self.name = name
        # Change balance to __balance to ask Python to hide it by name mangling
        self.__balance = balance
        print("Create account for {}".format(self.name))

    # Optional return type hint with "->"
    def deposit(self, amount: int) -> float:
        if amount > 0:
            self.__balance += amount
            # ":5.2f" specifies width field and type
            print("${:5.2f} deposited".format(amount /100))
        else:
            print("Error: amount must be > 0")
        return self.__balance/100

    def withdraw(self, amount: int) -> float:
        if 0< amount <= self.__balance:
            self.__balance -= amount
            # Note "6" gives more space than 5 in deposit method
            print("${:10.3f} withdraw".format(amount / 100))
            return self.__balance / 100
        else:
            print("Error: withdraw amount must be > 0 and less than balance")
            return self.__balance / 100

    def show_balance(self):
        print("Balance: ${:.3f}".format(self.__balance/100))


if __name__ == "__main__":
    # Note: the amount is in cents
    mickey = Account("Mickey", 1010)
    mickey.show_balance()

    mickey.deposit(10)
    mickey.deposit(10)
    mickey.withdraw(30)

    mickey.show_balance()

