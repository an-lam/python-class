import paramiko

hostname = '10.203.35.153'
port = 22
username = 'pi'
password = 'raspberry'

def copy_file(hostname, port, username, password, src, dst):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    print(" Connecting to {} with username = {}\n".format(hostname,username))
    t = paramiko.Transport(hostname, port)
    t.connect(username=username,password=password)
    sftp = paramiko.SFTPClient.from_transport(t)
    print("Copying file: {} to path: {}".format(src, dst))
    sftp.put(src, dst)
    sftp.close()
    t.close()

if __name__ == "__main__":
    print("Calling copy_file:\n")
    src = ???
    dst = ???
    copy_file(hostname, port, username, password, src, dst)
