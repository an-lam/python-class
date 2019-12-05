import sqlite3
from datetime import datetime
from ssh_connection import SSHconnection

db = sqlite3.connect("testrecords.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS testrecords (testid TEXT PRIMARY KEY NOT NULL, "
           "testname TEXT NOT NULL, lastresult TEXT, lastrun TIMESTAMP)")


#hostname = '10.203.35.153'
hostname = '192.168.2.36'
port = 22
username = 'pi'
password = 'raspberry'

def test_ls():
    ssh_con = SSHconnection(hostname, username, password, port)
    out, err = ssh_con.execute_command("ls /home/pi")
    print("output from Raspberry Pi: " + out)

    if out == "":
        result = "fail"
    else:
        result = "pass"

    testid = 1234
    testname = "test_ls"
    testtime = str(datetime.now())
    db.execute("INSERT INTO testrecords VALUES(?, ?, ?, ?)",
               (testid, testname, result, testtime))
    db.commit()

    ssh_con.close()
    assert out != ""


def test_ls_update():
    ssh_con = SSHconnection(hostname, username, password, port)
    out, err = ssh_con.execute_command("ls /home/pi")
    print("output from Raspberry Pi: " + out)

    if out == "":
        result = "fail"
    else:
        result = "pass"

    testid = 1234
    testname = "test_ls"
    testtime = str(datetime.now())
    db.execute("UPDATE testrecords SET testtime = ? WHERE (testid = ?)",
               (testtime, testid))
    db.commit()

    ssh_con.close()
    assert out != ""

def test_ls_negative():
    ssh_con = SSHconnection(hostname, username, password, port)
    # Pass test:
    # out, err = ssh_con.execute_command("ls /not_exists")

    # Fail test:
    out, err = ssh_con.execute_command("ls /home/pi")

    if out != "":
        result = "fail"
    else:
        result = "pass"

    testid = 56872
    testname = "test_ls_negative"
    testtime = str(datetime.now())
    print("time = " + testtime)
    db.execute("INSERT INTO testrecords VALUES(?, ?, ?, ?)",
               (testid, testname, result, testtime))

    db.commit()
    ssh_con.close()

def print_results():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM testrecords")
    # Load all rows into memory
    print("Result table:")
    print(cursor.fetchall())
    cursor.close()
    db.close()

def print_one(testid)
    cursor = db.cursor()
    cursor = db.execute("SELECT testname, result FROM testrecords WHERE (testid = ?)", (testid,))
    row = cursor.fetchone()
    print(row)

if __name__ == "__main__":
    print("Calling test_ls:\n")
    test_ls()

    print("Calling test_ls_negative:\n")
    test_ls_negative()

    print_results()

    print_one(56872)
