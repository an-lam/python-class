import sqlite3

db = sqlite3.connect("contacts.sqlite")

# db.execute("CREATE TABLE contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts(name, phone, email) VALUES('Mickey', 8876590, 'mickey@disney.com')")
#db.execute("INSERT INTO contacts VALUES('Minni', 9876, 'minni@disney.com')")
db.execute("INSERT INTO contacts VALUES('Goofey', 9876, 'minni@disney.com')")

cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")

# Load all rows into memory (return a list)
#print(cursor.fetchall())

# Get one row at a time
print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())
#cursor.close()
print(cursor.fetchall())

cursor.close()
db.commit()
db.close()