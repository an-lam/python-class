import sqlite3

db = sqlite3.connect("devices.sqlite")

# Continue next line by using "\"
db.execute("CREATE TABLE IF NOT EXISTS devices (ip_address TEXT PRIMARY KEY NOT NULL, location TEXT \
           serial INTEGER, model TEXT)")

def insert_device(ip, location, serial, model):
    db.execute("INSERT INTO devices VALUES (?, ?, ?)", (ip, location, serial))


def list_device(ip):
    cursor = db.execute("SELECT * FROM  devices WHERE ip_address = ?", (ip,))
    print(cursor.fetchone())

def list_all():
    cursor = db.execute("SELECT * FROM  devices")

    for row in cursor:
        print(row)

ip = "22.33.44.55"
insert_device(ip, "San Jose", 98765, "NAS-100")
list_device(ip)

ip = "243.5.10.98"
# Error if ip exists in devices
insert_device(ip, "Santa Clara", 5672345, "NAS-400")

list_device("22.33.44.55")       # None

#list_all()


db.commit()
db.close()
