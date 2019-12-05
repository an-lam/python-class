# test_commands.py

from ssh_connection import SSHconnection

# An Lam's RP
#hostname = '192.168.128.32'
hostname = '10.0.0.21'
port = 22
username = 'pi'
password = 'anlam2018'
# password = 'lam2018'
"""
hostname = '192.168.1.131'
port = 22
username = 'pi'
password = 'raspberry'
"""

def test_dmesg():
    ssh_con = SSHconnection(hostname, username, password, port)
    out, err = ssh_con.execute_command_buffer("dmesg")
    print("output from Raspberry Pi: " + out)
    # assert out == ""
    #assert out != ""
    ssh_con.close()

def test_top():
    ssh_con = SSHconnection(hostname, username, password, port)
    out, err = ssh_con.execute_command_buffer("top")
    print("output from Raspberry Pi: " + out)
    # assert out == ""
    #assert out != ""
    ssh_con.close()

def test_any_command(cmd):
    err = ""
    ssh_con = SSHconnection(hostname, username, password, port)
    out, err = ssh_con.execute_command(cmd)
    if err != "":
        print(err)

    print("output from '{}': \n {}".format(cmd, out))
    ssh_con.close()

if __name__ == "__main__":
    print("Calling test_dmesg:\n")
    # test_dmesg()

    print("Calling test_any_command")
    cmd = "ls -l /home/pi"
    #cmd = "ls /bin"
    # cmd = "ls -l /notexist"
    #cmd = "top "
    test_any_command(cmd)

    #test_top()


