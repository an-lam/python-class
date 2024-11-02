
while True:
    ip = input("\nIP: ")
    ip_address = ip.split(".")
    valid = True
    if len(ip_address) != 4:
        valid = False
        print("Invalid ip")
    elif ip == "0.0.0.0":
        valid = False
        print("Invalid IP.  It should have 4 number from 0 to 255 and seperate by 3 period.")
    else:
        for i in ip_address:
            if not i.isdigit():
                valid = False
                print("Invalid IP.  It should have seperate by 3 period.")
            elif int(i) < 0 or int(i) > 255:
                valid = False
                print("Invalid IP.  It should have 4 number from 0 to 255 and seperate by 3 period.")
            else:
                #print(ip)
                print("____"*40)
                break

    def setting_dict(devices):
            #ip = dictionary key, values = location, model, serial
            #ask user for each value
        ip = key
        for key, value in devices:
            if ip == "quit" or ip == 'q':
                print(ip)
            else:
                print("This is already in database.  Please enter another one.")
                location = input("Enter location: ")
                model = input("Enter model: ")
                serial = input("Enter serial:")
                devices[ip] = {"location": location, "model": model,"serial": serial}
                print(devices[ip])



"""
def setting_edit(devices):
    retrieved_ip_address = input("would you like to retrieve setting?")
    #if ip_list == {}:
     #   print("The database is empty.")
    #else:
    for key in devices:
        #retrieve_ip = "key"
        ip == key
    if retrieved_ip_address == 'yes':
        data = input('Which ip would you like to retrieve?')
        print('Here is the data for: {}'.format(data))
        change = input("Would you lke to make any change?")
        if change == "yes":
            change = input("Which would you like to change?: (location, model, serial)")
            if change == "location":
                location = input("which is new location?: ")
                print("change{}".format(location))
                return
            elif change == "model":
                model = input("which is new model?: ")
                print("change{}".format(model))
            elif change == "serial":
                serial = (input("which is new serial?: "))
                print("change{}".format(serial))
            else:
                print("Error! You did not input to change any data.")
        else:
            return True
    else:
        print("IP does not exit.  Here are the data in the database: ")
        print(ip_list)
"""

devices = ip = {}
setting_dict(devices)
#setting_edit(devices)