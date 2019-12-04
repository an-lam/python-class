import sqlite3
from datetime import datetime, timedelta

# Create a connection object
db = sqlite3.connect("accounts.sqlite")

# name-> PRIMARY KEY NOT NULL: name must be unique in the 'accounts' table
db.execute("CREATE TABLE IF NOT EXISTS accounts (name TEXT PRIMARY KEY NOT NULL UNIQUE, balance INTEGER NOT NULL)")
db.execute("CREATE TABLE IF NOT EXISTS transactions (time TIMESTAMP NOT NULL,"
           " account TEXT NOT NULL, amount INTEGER NOT NULL, PRIMARY KEY (time, account))")


class Account

    @staticmethod
    def _cur_time():
        return str(datetime.now())

    def __init__(self, name: str, opening_balance: int = 0):
        cursor = db.execute("SELECT name, balance FROM accounts WHERE (name = ?)", (name,))
        # Get the next row from the query result
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
        amount /= 100
        new_balance = self._balance + amount
        deposit_time = Account._cur_time()
        db.execute("UPDATE accounts SET balance = ? WHERE (name = ?)", (new_balance, self.name))
        db.execute("INSERT INTO transactions VALUES(?, ?, ?)", (deposit_time, self.name, amount))
        db.commit()
        self._balance = new_balance

    def show_balance(self):
        print("Balance on account {} is {:.2f}".format(self.name, self._balance / 100))

    def show_transactions(self):
        print("Transactions for account: {}".format(self.name))
        for row in db.execute("SELECT * FROM transactions WHERE (account = ?)", (self.name,)):
            time, account, amount = row
            print("time: {}, account: {}, amount: {}".format(time, account, amount))
            now = Account._cur_time()
            #if time < now:
            #    print(time, now)

if __name__ == '__main__':
    mickey = Account("Mickey")
    mickey.deposit(1010)
    mickey.deposit(10)
    mickey.deposit(10)
    mickey.withdraw(30)
    mickey.withdraw(0)
    mickey.show_balance()
    mickey.show_transactions()

    today = datetime.now()
    pastdate = today - timedelta(days=2, hours=1, minutes=10, seconds=20)
    print(pastdate)

    mini = Account("Mini", 200*100)
    tom = Account("Tom")
    jerry = Account("Jerry", 9000)
    jerry2 = Account("Jerry2", 2000*100)
    miney = Account("Miney", 7000)
    tom.deposit(100*100)
    tom.withdraw(30*100)
    tom.show_transactions()

    db.close()
