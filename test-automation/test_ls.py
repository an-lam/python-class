# test_ls.py

from ssh_connection import SSHconnection

hostname = '10.0.0.7'
port = 22
username = 'pi'
password = 'anlam2018'

def test_ls():
    ssh_con = SSHconnection(hostname, username, password, port)
    out, err = ssh_con.execute_command("ls /home/pi")
    print("output from Raspberry Pi: " + out)
    # assert out == ""
    assert out != ""
    ssh_con.close()

def test_ls_negative():
    ssh_con = SSHconnection(hostname, username, password, port)
    out, err = ssh_con.execute_command("ls /not_exists")
    if out != "":
        print("output from Raspberry Pi: " + out)
        raise FileExistsError("Expect error")

    assert err == ""
    ssh_con.close()

if __name__ == "__main__":
    print("Calling test_ls:\n")
    test_ls()

    print("Calling test_ls_negative:\n")
    test_ls_negative()
