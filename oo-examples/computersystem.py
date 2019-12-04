# computersystem.py
from device import Device

""" This class represents a computer system

"""

class ComputerSystem(Device):
    """Class represents a computer system

    Attributes:
        ip_addr (str): the IP address of the computer
        location (str): where the computer resides
        _os (str): the operating system of this computer

    Note: Read Python Docstring convention
    https://www.python.org/dev/peps/pep-0257/
    """

    def __init__(self, ip_addr, location, vendor="Dell"):
    #def __init__(self, ip_addr, location, vendor):
        # Call super class method to set ip_addr and location
        super().__init__(ip_addr, location)
        self._vendor = vendor

    #def __get_ip_addr(self):
    #    return self.ip_addr

    def ls(self):
        # "pass": Place holder for subclass to implement
        pass

    def copy(self):
        # "pass": Place holder for subclass to implement
        pass

    # Note: no setter method for OS because it's set only when an
    # OS is installed
    def install_os(self, osname, osfile):
        # install OS from osfile
        # set osname
        self._os = osname

    def _get_os(self):
        """
           Get OS name installed on the computer system
        :return (str): OS name
        """
        return self._os

    osname = property(_get_os)

    # Using decorator
    @property
    def manufacturer(self):
        print("in manufacturer getter method")
        return self._vendor

    @manufacturer.setter
    def manufacturer(self, vendor):
        print("in manufacturer setter method")
        self._vendor = vendor

    def __str__(self):
        return "IP address: {0.ip_addr}, location: {0.location}, OS: {0._os}, manufacturer: {0._vendor}".format(self)

