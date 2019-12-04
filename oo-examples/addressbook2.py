import sqlite3

db = sqlite3.connect("contacts.sqlite")

# db.execute("CREATE TABLE contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts(name, phone, email) VALUES('Mickey', 8876590, 'mickey@disney.com')")
db.execute("INSERT INTO contacts VALUES('Minni', 456788, 'minni@disney.com')")
db.execute("INSERT INTO contacts VALUES('Minni', 897654, 'minni2@disney.com')")

cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")
for name, phone, email in cursor:
    print("name: {}, phone: {}, email: {}".format(name, phone, email))
    print("-" * 20)

db.commit()
cursor.close()
db.close()
"""
If you see error: 
 File "C:/Users/lama2/PycharmProjects/ooconcepts/addressbook2.py", line 17, in <module>
    db.commit()
sqlite3.OperationalError: database is locked

Exit Pycharm and re-open because another thread still holds the lock in previous run
"""