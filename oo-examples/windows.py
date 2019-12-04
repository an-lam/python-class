# windows.py
from computersystem import ComputerSystem
import os

""" This class represents a computer host

"""

class Windows(ComputerSystem):
    """Class represents a computer system

    Attributes:
        ip_addr (str): the IP address of the computer
        location (str): where the computer resides
        _os (str): the operating system of this computer

    Note: Read Python Docstring convention
    """

    #def __init__(self, ip_addr, location):
     #   """Host init method
      #  :param ip_addr (str): initialize the IP address
     #   :param location (str): initialize the location
      #  """
     #   self.ip_addr = ip_addr
     #   self.location = location
     #   self._version = 0    # caller should not change version directly
      #  self._os = "Windows 10"

    def ls(self, directory):
        """
           List current directory contents.

        :param directory:
        :return:
        """
        return os.listdir(directory)

    def copy(self, source, destination):
        """
         Copy a file to a new file
         Note: Pycharm automatically fills out :param tag for you
        :param source: the source (orginal) file name
        :param destination: the new file name
        :return: None
        """
        """
        try:
            os.system("copy {} {}".format(source, destination))
        # os.system doesn't throw exception
        # it returns 0 or 1.  So, 'except' won't catch anything here
        except FileNotFoundError as err:
            print("Exception: {}".format(err))
        except:
            print("Exception")
        else:
            print("File copy successfully.")
        """
        code = os.system("copy {} {}".format(source, destination))
        if code == 1:
            print("Copy fails.")

    def __str__(self):
        return "IP address: {0.ip_addr}, location: {0.location}, OS: {0._os}".format(self)

if __name__ == "__main__":
    windows1 = Windows("2.4.5.6", "San Jose", "Windows 10")
    print(windows1)

    print("List current directory:")
    print(windows1.ls("."))

    print("Copy a file: ")
    source = input("Enter source file:")
    destination = input("Enter new file name:")
    windows1.copy(source, destination)
    #print("--" * 40)
    #print all docstring info
    #help(Windows)

    # print help on specific method
    #help(Windows.copy)
