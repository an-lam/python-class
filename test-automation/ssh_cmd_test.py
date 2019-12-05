import paramiko
import time

# An Lam's Raspberry's credentials:
address = '172.16.0.21'
username = 'pi'
password = 'anlam2018'
port = 22

class ssh:
    client = None

    def __init__(self, address, port, username, password):
        print("Connecting to server.")
        # Create a new SSH client
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(address, port, username, password)

    def sendCommand(self, command):
        if self.client:
            # The output of command goes to stdout
            stdin, stdout, stderr = self.client.exec_command(command)
            file_name = command.replace("/", "")        # remove all "/" chars in command
            file_name += ".txt"
            file = open(file_name)
            print('File "{}" is opened!' .format(file_name))
            cmd_passed = False
            fail_token = False
            exitStatus = True

            # How to use channel document: http://docs.paramiko.org/en/2.4/api/channel.html
            while not stdout.channel.exit_status_ready():
                exitStatus = False
                time.sleep(2)

                # Read data if it's ready in buffer from server (recv_ready() returns true)
                if stdout.channel.recv_ready():
                    print("stdout.channel.recv ready")
                    alldata = stdout.channel.recv(1024)   # receive first 1024 bytes

                    # Continue to read data one buffer at a time
                    while stdout.channel.recv_ready():
                        time.sleep(2)
                        print("Receive the next 1024 bytes")
                        alldata += stdout.channel.recv(1024)

                    # string with utf8 encoding, then convert into list - with split()
                    recv_data = (str(alldata, "utf8")).split('\n')

                    for num, line in enumerate(file):
                        print("From server: {0}\nFrom file:   {1} " .format(recv_data[num].strip(),line.strip()))

                        if recv_data[num].strip() == line.strip():
                            cmd_passed = True
                        else:
                            cmd_passed = False
                            fail_token = True
                            print("Command {} failed because \nReceived from server: {} \nExpected:             {}"
                                  .format(command, recv_data[num], line))

                else:
                    print("stdout.channel.recv not ready")

            if exitStatus:
                print("stdout.channel status: exit")

            if cmd_passed and not fail_token:
                print('Command "{}" passed'.format(command))
            else:
                print('Command "{}" failed'.format(command))
            file.close()

        else:
            print("Connection not opened.")

if __name__ == "__main__":
    connection = ssh(address, port, username, password)

    connection.sendCommand("ls")
    time.sleep(120)
    #connection.sendCommand("lsusb")
    #time.sleep(120)
    #connection.sendCommand("dmesg")
    #time.sleep(120)
    #connection.sendCommand("cat /proc/cpuinfo")
    connection.client.close()
    #file.close()



