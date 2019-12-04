# compmain.py

from computersystem import ComputerSystem
from windows import Windows

#device1 = Device("San Jose")
#device1.set_ip_address("41.2.3.4")

computer1 = ComputerSystem("87.90.11.0", "San Jose", "HP")

print(computer1)
#print(computer1.__get_ip_addr()) # violate the rule
print("Getting osname:")
print(computer1.osname)
#computer1.osname = "Linux"
print("\n Setting ip_addr:")
computer1.ip_addr = "1.2.3.4"

print("Getting ip_addr:")
print(computer1.ip_addr)

# Setting osname indirectly by installing OS
computer1.install_os("Windows 10", "windows.zip")
#computer1.osname = "Linux"  # Error, no setter method for osname
print(computer1.osname)

print(computer1._version)

computer2 = ComputerSystem("4.3.2.1", "Santa Clara")
# Calling setter method
print("\n Setting manufacturer:")
computer2.manufacturer = "HP"

# Calling getter method
print(computer2.manufacturer)