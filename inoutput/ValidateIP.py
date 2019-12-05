# Program: Read a string in input and validate whether or not it is a valid IP address
# Class: Python Programming
# Student: Simon Lam

# import sets

def checkIPFormat(ipFieldList):
    ipInvalid = False;
    ipFieldInvalid = False;
    
    for i in range(0, len(ipFieldList)):
        ipField = ipFieldList[i];
            
        if (ipField in (['', ' '])):
            ipInvalid = True;
            print("The ip address contains empty field.");
            break;
        
        for j in range(0, len(ipField)):
            if (not (ipField[j].isdigit())):
                ipFieldInvalid = True;
                print("The sub ip address field contains invalid format for: " + ipFieldList[i]);
                break;
        if (ipFieldInvalid == True):              
            ipInvalid = True;
            break;
            
        if (0 <= int(ipFieldList[i]) <= 255):
            ipInvalid = False;
        else:
            ipInvalid = True;
            print("The ip address is out of range of 0 - 255: {}".format(ipFieldList[i]));
            break;
    return (ipInvalid);

validIPs = set();
invalidIPs = set();

def validateIPAddress():
    while (True):
        ip = input("\nPlease enter an ip address or quit(q) to finish entering: ");
    
        if (ip == "quit" or ip == "q"):
            print();
            print("These are Invalid IP addresses entered: ");
            print(sorted(invalidIPs));
            print("These are Valid IP addresses entered: ");
            print(sorted(validIPs));
            # break;
            return ip;
        if (ip == "0.0.0.0"):
            print(ip + " is not a valid ip address.");
            invalidIPs.add(ip);
            continue;
    
        ipFieldList = ip.split(".");
        if (len(ipFieldList) != 4):
            print("The entered ip address must have 4 fields.");
            print("Valid format: 0-255.0-255.0-255.0-255");
            invalidIPs.add(ip);
        else:
            if (ip in validIPs):
                print(ip + " is duplicate of a valid ip address.");
            elif (ip in invalidIPs):
                print(ip + " is duplicate of an invalid ip address.");
            else:
                ipInvalid = checkIPFormat(ipFieldList);
                if (ipInvalid == False):
                    print(ip + " is a valid ip address!");
                    validIPs.add(ip);
                    return ip;
                else:
                    invalidIPs.add(ip);

if __name__ == "__main__":
    validateIPAddress();
