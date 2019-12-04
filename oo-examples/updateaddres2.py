# How to substitute variables in SQL statements

import sqlite3

db = sqlite3.connect("contacts.sqlite")

new_email = input("Please enter your new e-mai: ")
phone = input("Please enter your phone: ")

#update_stm = "UPDATE contacts SET email = 'newemail@disney.com' WHERE contacts.phone = 9876"
update_stm = "UPDATE contacts SET email = ? WHERE phone = ?"
print(update_stm)

update_cursor = db.cursor()
# Substitute ? with values, then update the row
update_cursor.execute(update_stm, (new_email, phone))
#update_cursor.execute(update_stm, (phone, new_email))
print("{} rows updated".format(update_cursor.rowcount))

update_cursor.connection.commit()
update_cursor.close()

# Unpack data into different variable
print("\n Contacts in DB:")
for name, phone, email in db.execute("SELECT * FROM contacts"):
    print(name)
    print(phone)
    print(email)
    print("-" * 20)

# If you don't commit, changes will not be saved
# NOTE: if you get error: "DB is locked" click on the table name on the right hand panel
# and disconnect from DB.  DB Navigator locks the table.
db.commit()
db.close()