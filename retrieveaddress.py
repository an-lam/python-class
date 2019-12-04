# Retrieve records from existing table
import sqlite3

db = sqlite3.connect("contacts.sqlite")

# If this loop doesn't print  anything, debug addressbook.py ?
for row in db.execute("SELECT * FROM contacts"):
    print(row)

# Unpack data into different variable
for name, phone, email in db.execute("SELECT * FROM contacts"):
    print(name)
    print(phone)
    print(email)
    print("-" * 20)

db.close()