import paramiko

hostname = '10.0.0.211'
port = 22
username = 'lvu'
password = 'test1234'

if __name__ == "__main__":
    paramiko.util.log_to_file('paramiko.log')
    sclient = paramiko.SSHClient()
    # s.set_missing_host_key_policy(paramiko.WarningPolicy)
    sclient.set_missing_host_key_policy(paramiko.client.AutoAddPolicy)
    sclient.load_system_host_keys()
    sclient.connect(hostname, port, username=username, password=password)
    stdin, stdout, stderr = sclient.exec_command('ls /')
    #outString = stdout.readline()
    outString = stdout.read().decode()
    print(" Output from Rasberry Pi: " + outString)

    sclient.close()