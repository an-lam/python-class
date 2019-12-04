import sqlite3

"""
    SQLITE documents:
    http://www.sqlite.org/
    
    Create table syntax:
    http://www.sqlite.org/lang_createtable.html
"""

db = sqlite3.connect("contacts.sqlite")

# Create a new table everytime.  That's not our intention
# db.execute("CREATE TABLE contacts (name TEXT, phone INTEGER, email TEXT)")

# Create new table only if it doesn't exist yet
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")

db.execute("INSERT INTO contacts(name, phone, email) VALUES('Mickey', 8876590, 'mickey@disney.com')")
db.execute("INSERT INTO contacts VALUES('Minni', 1234, 'minni@disney.com')")

cursor = db.cursor()
# cursor is fetched one row at a time
cursor.execute("SELECT * FROM contacts")
for name, phone, email in cursor:
    print("name: {}, phone: {}, email: {}".format(name, phone, email))
    print("-" * 40)

cursor.close()
db.commit()
db.close()
# Where is our data?  The DB is there, but there is no record.
# What's wrong?