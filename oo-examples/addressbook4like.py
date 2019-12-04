import sqlite3

db = sqlite3.connect("contacts.sqlite")

name = input("Please enter your name to retrieve address: ")

# Unpack data into different variable
print("\n Your contact info:")
#for row in db.execute("SELECT * FROM contacts WHERE name = ?", (name,)):
# Use LIKE to ignore case-sensitive
# Note: (name,) : parentheses are important because we need to pass in
# a tuple (not a single variable)
#for row in db.execute("SELECT * FROM contacts WHERE name LIKE ?", name):  # Error
for row in db.execute("SELECT * FROM contacts WHERE name LIKE ?", (name,)):
    print(row)

# commit is not needed, why ?
db.close()