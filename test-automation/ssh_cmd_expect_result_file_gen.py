import paramiko
import time

# Raspberry's credentials:
address = '192.168.1.84'
username = 'pi'
password = 'raspberry'
port = 22

class ssh:
    client = None

    def __init__(self, address, port, username, password):
        print("Connecting to server.")
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(address, port, username, password)

    def sendCommand(self, command):
        # Check if connection is made previously
        if (self.client):
            stdin, stdout, stderr = self.client.exec_command(command)
            file_name = command.replace("/", "")
            file_name += ".txt"
            file = open(file_name, "w")
            while not stdout.channel.exit_status_ready():
                time.sleep(2)
                # "stdout data when available"
                if stdout.channel.recv_ready():
                    print("Retrieve the first 1024 bytes")
                    alldata = stdout.channel.recv(1024)
                    while stdout.channel.recv_ready():
                        time.sleep(2)
                        print("Retrieve the next 1024 bytes")
                        alldata += stdout.channel.recv(1024)

                    print("str all data: ", str(alldata, "utf8"))
                    print("all data: ", (alldata, "utf8"))
                    file.write(str(alldata, "utf8"))
            file.close()
        else:
            print("Connection not opened.")

if __name__ == "__main__":
    connection = ssh(address, port, username, password)

    connection.sendCommand("ls")
    #connection.sendCommand("lsusb")
    #connection.sendCommand("cat /proc/cpuinfo")
    #connection.sendCommand("dmesg")

    connection.client.close()



