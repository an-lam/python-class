# test_ls.py
from SFTPConn import SFTPConn
from ssh_connection import SSHconnection

#hostname = '10.110.142.143'   # dd860-119.chaos.local
hostname = "dd7200-48.datadomain.com"
#hostname = "dd620-23.chaos.local"
port = 22
username = "root"
password = "abc123"

def test_ls():
    ssh_con = SSHconnection(hostname, username, password, port)
    cmd1 = "ls -l /usr"
    out, err = ssh_con.execute_command(cmd1)
    print("output from Linux host {}: ".format(hostname, out))
    # assert out == ""
    assert out != ""
    ssh_con.close()

def test_put_file():
    # This method put a file on Linux successfully
    sftp_conn = SFTPConn(hostname, username, password)
    local_file = 'test_anlam_linux.py'
    remote_file = '/var/tmp/test_anlam_linux.py'
    sftp_conn.put(local_file, remote_file)
    print("Put file {} ".format(remote_file))

if __name__ == "__main__":
    print("Calling test_ls:\n")
    test_ls()

    #print("Calling put_file\n")
    #test_put_file()
