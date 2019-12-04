import sqlite3

db = sqlite3.connect("contacts.sqlite")

# db.execute("CREATE TABLE contacts (name TEXT, phone INTEGER, email TEXT)")
#db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
#db.execute("INSERT INTO contacts(name, phone, email) VALUES('Mickey', 8876590, 'mickey@disney.com')")
#db.execute("INSERT INTO contacts VALUES('Minni', 456788, 'minni@disney.com')")

cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")
for name, phone, email in cursor:
    print("name: {}, phone: {}, email: {}".format(name, phone, email))
    print("-" * 20)


cursor.close()
db.close()