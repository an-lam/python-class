# Update statement for specific row

import sqlite3

db = sqlite3.connect("contacts.sqlite")

update_stm = "UPDATE contacts SET email = 'email@disney.com' WHERE contacts.phone = 1234"
update_cursor = db.cursor()
update_cursor.execute(update_stm)

print("{} rows updated".format(update_cursor.rowcount))

# Unpack data into different variable
for name, phone, email in db.execute("SELECT * FROM contacts"):
    print(name)
    print(phone)
    print(email)
    print("-" * 20)

# If you don't commit, changes will not be saved
db.commit()
db.close()