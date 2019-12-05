# lab4main.py
#import lab4library
from lab4library import validateIP
"""
ip1 = "1.8.3.4"
if lab4library.validateIP(ip1):
    print("Valid IP = {}".format(ip1))
else:
    print("Invalid IP = {}".format(ip1)) 
"""
ip1 = "1.25.3.6"
if validateIP(ip1):
    print("Valid IP = {}".format(ip1))
else:
    print("Invalid IP = {}".format(ip1))



# These are some examples how to keep track of devices using IP address
# as keys

# devices = {}
# property1 = "location: San Jose, model: NAS-100, serial: 12345"
# devices[ip1] = property1
#
# property2 = {}
# property2["location"] = "Santa Clara"
# property2["model"] = "NAS-200"
# property2["serial"] = 98978655
# ip2 = "55.35.6.7"
# devices[ip2] = property2
#
# print(devices)
#
# #ip3 = "2.3.4"
# ip3 = ip2
# if ip3 in devices:
#     print(devices[ip3])
# else:
#     print("Device does not exist.")
