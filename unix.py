# unix.py
import os
from computersystem import ComputerSystem
#import os

""" This class represents a Unix computer
"""

class Unix(ComputerSystem):
    """Class represents a Unix computer system

    Attributes:
        ip_addr (str): the IP address of the computer
        location (str): where the computer resides
        _os (str): the operating system of this computer

    Note: Read Python Docstring convention
    """

    # def __init__(self, ip_addr, location):
    #     """Host init method
    #     :param ip_addr (str): initialize the IP address
    #     :param location (str): initialize the location
    #     """
    #     self.ip_addr = ip_addr
    #     self.location = location
    #     self._version = 0    # caller should not change version directly
    #     self._os = "None"

    def ls(self, directory):
        return (os.system("ls {}".format(directory)))

    def copy(self, source, destination):
        print("in Unix.copy()")
        os.system("cp {} {}".format(source, destination))

    #def __str__(self):
    #     return "IP address: {0.ip_addr}, location: {0.location}, OS: {0._os}".format(self)

class Linux(Unix):
    pass

if __name__ == "__main__":
    unix_sys = Unix("88.4.55.166", "San Clara")
    print(unix_sys)

    print("List current directory:")
    print(unix_sys.ls("."))

    lnx = Linux("5.4.2.1", "San Jose")
    print(lnx.ip_addr)
    print(lnx)
    lnx.copy("a", "b")

