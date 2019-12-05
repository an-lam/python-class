# Program: Building Devices' Inventory
# Class: Python Programming
# Student: Simon Lam

from ValidateIP import validateIPAddress
from ValidateIP import validIPs

def enterIPDeviceProperties():
    location = input("Please enter Location for the ip: ");
    model = input("Please enter Model for the ip: ");
    serial = input("Please enter Serial for the ip: ");
    while (serial in validSerial):
        print("Duplicate, serial number already exists!");
        serial = input("Please enter unique Serial for this ip: ");
    validSerial.add(serial);
    prop = [];
    prop = [location, model, serial];
    dictDevices[ip] = prop;

def getIPProperties(k, v):
    print('\nIP: {}'.format(k));
    for i in range(0, len(v)):
        if i == 0:
            print('Location: {} '.format(v[i]));
        if i == 1:
            print('Model: {} '.format(v[i]));
        if i == 2:
            print('Serial: {} '.format(v[i]));

def printIPNotValid():
    print("ERROR: ip does not exist to retrieve from the database!")
    print("These are Valid IP addresses in the database: ");
    print(sorted(validIPs));

def retrieveIPDeviceProperties():
    while (True):
        while(True):
            ruq = input("\nDo you want to retrieve(r) the properties of an ip address, or quit(q) to exit: ");
            if (ruq != "r" and ruq != "retrieve" and ruq != "update" and ruq != "u" and ruq != "quit" and ruq != "q"):
                print("Invalid Input!");
                continue;
            else:
                break;

        global ip;
        if (ruq == "r" or ruq == "retrieve"):
            ip = input("\nEnter ip address to retrieve the device properties or quit(q) to exit: ");
            if (ip == "quit" or ip == "q"):
                break;
            else:
                if not (ip in validIPs):
                    printIPNotValid();
                else:
                    v = dictDevices.get(ip);
                    getIPProperties(ip, v);

                    ruq = input("\nDo you want to: "
                                "\n1) update(u) the properties WITHOUT changing this device ip address,"
                                "\n2) change(c) the properties WITH changing the ip address for this device,"
                                "\n3) or quit(q) to exit: "
                                "\nEnter update(u) or change(c) or quit(q): ");
                    if (ip == "quit" or ip == "q"):
                        break;
                    elif (ruq == "update" or ruq == "u"):
                        devProp = dictDevices[ip];
                        validSerial.remove(devProp[2]);
                        enterIPDeviceProperties();
                    elif (ruq == "change" or ruq == "c"):
                        ruq = input("\nDo you want to: "
                                    "\n1) change ip address only and keep(k) the same properties for this device,"
                                    "\n2) change ip address but also alter(a) the properties for this device,"
                                    "\nEnter keep(k) or alter(a): ");
                        if (ruq == "keep" or ruq == "k"):
                            devProp = dictDevices[ip];
                            del dictDevices[ip];
                            validIPs.remove(ip);
                            ip = validateIPAddress();
                            dictDevices[ip] = devProp;
                        elif (ruq == "alter" or ruq == "a"):
                            devProp = dictDevices[ip];
                            validSerial.remove(devProp[2]);
                            del dictDevices[ip];
                            validIPs.remove(ip);
                            ip = validateIPAddress();
                            enterIPDeviceProperties();
                        else:
                            print("Invalid Input!")

        if (ruq == "quit" or ruq == "q"):
            break;

def buildDeviceInventory():
    while (True):
        global ip;
        ip = validateIPAddress();
        if (ip == "quit" or ip == "q"):
            break;
        else:
            enterIPDeviceProperties();
            retrieveIPDeviceProperties();
    print('\nCOMPLETE LIST OF DEVICE INVENTORY');
    print('=================================');
    for k, v in dictDevices.items():
        getIPProperties(k, v);

ip = "";
dictDevices = {};
validSerial = set();

if __name__ == "__main__":
    buildDeviceInventory();


