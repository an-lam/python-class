# lab4library.py

def validateIP(ip_address):
    items = ip_address.split('.')
    print(items)
    if (len(items) != 4):
        print("IP address {} does not have 4 digits.".format(ip_address))
        return False
    elif ip_address == "0.0.0.0":
        print("IP contains 4 zeros: {}".format(ip_address))
        return False

    # Check for digits
    good = True
    error = ""
    for i in items:
        print(i)
        if not (i.isdigit()):
            print("invalid digit {} ".format(i))
            error += " invalid digit " + str(i)
            good = False
            #return False
        elif int(i) > 255:
            print("network address {} > 255".format(i))
            error += " invalid integer value " + str(i)
            good = False
            #return False

    # IP address passes all checks
    print(error)
    return good

# Self-test code
# Executed when run, but not executed when import
if __name__ == "__main__":
    #ip = "9.1.988.-9"
    ip = "11.2.33.77.15"
    ip = "0.0.0.0"
    ip = input("Enter an IP address: ")
    #good = validateIP(ip)
    if (validateIP(ip)):
        print("good IP")
    else:
        print("invalid IP")