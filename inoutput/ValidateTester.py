import DeviceLib
devices = {}
while True:
    print("Enter an IP address: (quit to end): ")
    ip_address = input()
    if ip_address == "quit":
        break

    if not DeviceLib.validate_ip_address(ip_address):
        continue
    if DeviceLib.is_IP_in_DB(ip_address, devices):
        print("There is alredy a device located at the ip adreess: {}".format(ip_address))
        continue
    device = DeviceLib.create_device()
    devices[ip_address] = device

while True:
    print("Enter the IP address of the device that you would like (quit to end): ")
    ip_address = input()
    if ip_address == "quit":
        break

    if not DeviceLib.validate_ip_address(ip_address):
        continue

    if not DeviceLib.is_IP_in_DB(ip_address, devices):
        DeviceLib.IP_not_found(ip_address, devices)
    else:
        device = devices.get(ip_address)
        DeviceLib.print_device_properties(ip_address, device)
        if DeviceLib.would_like_to_make_change_to_device():
            DeviceLib.change_device_properties(device)



