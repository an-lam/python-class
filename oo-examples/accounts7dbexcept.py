import sqlite3
from datetime import datetime

"""
   Account class with exception and rollback
"""
# Create a connection object
db = sqlite3.connect("accounts.sqlite")


db.execute("CREATE TABLE IF NOT EXISTS accounts (name TEXT PRIMARY KEY NOT NULL, balance INTEGER NOT NULL)")
db.execute("CREATE TABLE IF NOT EXISTS transactions (time TIMESTAMP NOT NULL,"
           " account TEXT NOT NULL, amount INTEGER NOT NULL, PRIMARY KEY (time, account))")


class Account:

    @staticmethod
    def _current_time():
        return str(datetime.now())

    def __init__(self, name: str, opening_balance: int = 0):
        cursor = db.execute("SELECT name, balance FROM accounts WHERE (name = ?)", (name,))
        row = cursor.fetchone()

        # if row is not None:
        if row:
            self.name, self._balance = row
            print("Retrieved record for {}. ".format(self.name), end='')
        else:
            self.name = name
            self._balance = opening_balance
            cursor.execute("INSERT INTO accounts VALUES(?, ?)", (name, opening_balance))
            cursor.connection.commit()
            print("Account created for {}. ".format(self.name), end='')
        self.show_balance()

    def deposit(self, amount: int) -> float:
        if amount > 0.0:
            self._save_update(amount)
            print("{:.2f} deposited".format(amount / 100))
        return self._balance / 100

    def withdraw(self, amount: int) -> float:
        if 0 < amount <= self._balance:
            self._save_update(-amount)
            print("{:.2f} withdrawn".format(amount / 100))
            return amount / 100
        else:
            print("The amount must be greater than zero and no more than your account balance")
            return 0.0

    def _save_update(self, amount):
        new_balance = self._balance + amount
        deposit_time = Account._current_time()
        try:
            db.execute("UPDATE accounts SET balance = ? WHERE (name = ?)", (new_balance, self.name))
            db.execute("INSERT INTO transactions VALUE(?, ?, ?)", (deposit_time, self.name, amount))
        except sqlite3.Error as error:
            print(error)
            db.rollback()
        else:
            db.commit()

        self._balance = new_balance

    def show_balance(self):
        print("Balance on account {} is {:.2f}".format(self.name, self._balance / 100))

if __name__ == '__main__':
    mickey = Account("Mickey")
    mickey.deposit(1010)
    mickey.deposit(10)
    mickey.deposit(10)
    mickey.withdraw(30)
    mickey.withdraw(0)
    mickey.show_balance()

    tom = Account("Tom")
    jerry = Account("Jerry", 9000)
    miney = Account("Miney", 7000)

    db.close()
