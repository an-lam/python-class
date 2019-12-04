# device.py
""" This class represents a generic device
"""
class Device:
# or class Device:
    """Class represents a generic device
    Attributes:
        ip_addr (str): the IP address of the device
        location (str): where the device resides
        _os (str): the operating system of this device
    Note: Read Python Docstring convention
    """

    def __init__(self, ip_addr, location):
        """
        :param ip_addr:
        :param location:
        """
        self._ip_addr = ip_addr
        self.location = location
        self._version = 1    # caller should not change version directly
        self._os = "None"

    def _get_version(self):
        return self._version

    # Getter: prefix '_get<attribute-name>'
    def __get_ip_addr(self):
        print("in _get_ip_addr")
        return self._ip_addr

    # Setter: prefix '_set<attribute-name>'
    def set_ip_addr(self, ip_addr):
       print("in _set_ip_addr")
       self._ip_addr = ip_addr
       return self._ip_addr

    # Define setter and getter methods
    ip_addr = property(__get_ip_addr, set_ip_addr)

    def __str__(self):
        return "IP address: {0.ip_addr}, location: {0.location}, OS: {0._os}".format(self)

