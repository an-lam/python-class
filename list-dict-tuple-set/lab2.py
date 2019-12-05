# devices.py
location = input("Enter location")
model = input("Enter model")
serial = input("Enter serial")
ip_address = input("Enter IP address")

attr = [location, model, serial]
devices = {}
devices[ip_address] = attr

attr2 = {"location" : location, "model": model, "serial": serial}
devices[ip_address] = attr2

print(devices)
#devices = {"1.2.3.4": ("San Jose", "NAS-100", 1234)}

d2 = "Santa Clara", "NAS-200", 44321

devices["4.3.2.22"] = d2
print(devices["4.3.2.22"])

devices["6.7.88.0"] = ("SJ", "NAS-200", 567)
print(devices)
