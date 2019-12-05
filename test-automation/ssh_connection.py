# ssh_connection.py
"""
   This class establish an SSH Client connection to SSH Server
"""
import paramiko
import time

class SSHconnection(object):

    def __init__(self, hostname, input_username, input_password, port):
        self.host = hostname
        self.user = input_username
        self.password = input_password
        self.port = port

        self.sclient = paramiko.SSHClient()
        self.sclient.set_missing_host_key_policy(paramiko.client.AutoAddPolicy)
        self.sclient.load_system_host_keys()
        self.sclient.connect(hostname, port, timeout=3000, username=input_username, password=input_password)

    """
     Execute a command on RP and return output string
    :param command - command to be executed on Raspberry Pi
    :return outString - output from command
            errString - error message if command fails
    """
    def execute_command(self, command):
        print("ssh_connection::execute_command " + command)
        stdin, stdout, stderr = self.sclient.exec_command(command)
        outString = stdout.read().decode()
        errString = stderr.read().decode()
        print(" Output from device: " + outString)
        print(" errString : " + errString)
        return(outString, errString)

    """
        Execute a command on RP and return output string.  This method is
        used for commands that generate large data output.
    :param command - command to be executed on Raspberry Pi
    :return outString - output from command
            errString - error message if command fails
    """
    def execute_command_buffer(self, command):

        # Execute command on RP device
        stdin, stdout, stderr = self.sclient.exec_command(command)
        exitStatus = True

        outString = ""
        errString = stderr.read().decode()
        # If error is detected, get out of this method
        if errString != "":
            return (outString, errString)

        # Loop until the server sends 'exit' flag
        while not stdout.channel.exit_status_ready():
            exitStatus = False
            time.sleep(1)      # Wait for data to arrive

            if stdout.channel.recv_ready():
                print("stdout.channel.recv ready")
                # receive first 1024 bytes
                alldata = stdout.channel.recv(2048)

                # Receive data from server one buffer[2048] at a time
                while stdout.channel.recv_ready():
                    time.sleep(1)
                    print("Receive the next 2048 bytes")
                    alldata += stdout.channel.recv(2048)

                # Convert byte data from socket into string
                outString += str(alldata, "utf8")
            else:
                print("stdout.channel.recv not ready")

            if exitStatus:
                print("stdout.channel status: exit")

        return (outString, errString)


    """
        Close SSH socket
    """
    def close(self):
        self.sclient.close()
