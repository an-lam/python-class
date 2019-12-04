# Delete row using variable substitution

import sqlite3

db = sqlite3.connect("contacts.sqlite")

email = input("Please enter your e-mail to delete: ")

#update_stm = "UPDATE contacts SET email = 'newemail@disney.com' WHERE contacts.phone = 9876"
delete_stm = "DELETE FROM contacts WHERE email = ?"
print(delete_stm)

cursor = db.cursor()
#cursor.execute(delete_stm, (email))
cursor.execute(delete_stm, (email,))
print("{} rows deleted".format(cursor.rowcount))

cursor.connection.commit()
cursor.close()

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