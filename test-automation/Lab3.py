from device import Device

device_obj = Device()
try:
    print(" -" * 17)
    print ("|Type Ctrl-C to abort the program!|")
    print(" -" * 17)
    property_list = {}
    ip_list = []
    location = ''
    model = ''
    serial = ''
    while True:
        ip_addr = input('Please enter a valid ip address or type "q" or "quit" entering ip:')
        if ip_addr.lower() == 'q' or ip_addr.lower() == 'quit':
            if ip_list == []:
                print("You've not enter any IP yet. Please reenter your IP!")
                continue
            else:
                print("All IP address(s) have been entered.")
                break
        elif ip_addr in ip_list:
            print ('The IP address {} you\'ve entered already existed. Try again!'.format(ip_addr))
            continue
        elif device_obj.validate_ip_addr(ip_addr) == "False":
            continue
        else:
            print ('You\'ve entered your IP address: {}'.format(ip_addr))
            try:
                location = input("Please enter a location of your device:")
                model = input("Please enter a model of your device:")
                serial = input("Please enter a serial number of your device:")
                if location == '' or model == '' or serial == '':
                    raise ValueError ('One of the properties is empty!')
            except ValueError as err:
                print ('Input error: {}'.format(err))
            else:
                property_list['Location'] = location
                property_list['Model'] = model
                property_list['Serial'] = serial
                device_obj.configure_properties(ip_addr, **property_list)
                ip_list.append(ip_addr)
    while True:
        ip_addr_key = input("Please enter your IP address to retrieve device's properties:")
        if (device_obj.check_ip_in_database(ip_addr_key) == "True"):
            device_properties = input("Do you want to update device's properties? (y/yes or n/no)")
            if device_properties.lower() == 'n' or device_properties.lower() == 'no':
                continue
            elif device_properties.lower() == 'y' or device_properties.lower() == 'yes':
                print ('\tIP Address: '.format(ip_addr_key))
                device_obj.show_properties(ip_addr_key)
                selection = input(
                "Which device's property you'd like to update? (Type 'Location' for location, 'Model'"
                " for model, 'Serial' for serial, or 'All' for all):")
                if selection.lower() == 'all':
                    try:
                        modified_location = input("Please enter your modified location:")
                        modified_model = input("Please enter your modified model:")
                        modified_serial = input("Please enter your modified serial:")
                        if modified_location == '' or modified_model == '' or modified_serial == '':
                            raise ValueError ('One of modified properties is empty!')
                    except ValueError as err:
                        print ('Input error: {}'.format(err))
                        continue
                    else:
                        property_list['Location'] = modified_location
                        property_list['Model'] = modified_model
                        property_list['Serial'] = modified_serial
                        device_obj.configure_properties(ip_addr_key, **property_list)
                elif selection.lower() == 'location':
                    try:
                        modified_location = input("Please enter your modified location:")
                        if modified_location == '':
                            raise ValueError('Modified location can\'t be empty')
                    except ValueError as err:
                        print ('Input error: {}'.format(err))
                        continue
                    else:
                        property_list['Location'] = modified_location
                        device_obj.configure_properties(ip_addr_key, **property_list)
                elif selection.lower() == 'model':
                    try:
                        modified_model = input("Please enter your modified model:")
                        if modified_model == '':
                            raise ValueError('Modified model can\'t be emppty')
                    except ValueError as err:
                        print ('Input error: {}'.format(err))
                        continue
                    else:
                        property_list['Model'] = modified_model
                        device_obj.configure_properties(ip_addr_key, **property_list)
                elif selection.lower() == 'serial':
                    try:
                        modified_serial = input("Please enter your modfied serial:")
                        if modified_serial == '':
                            raise ValueError('Modified serial can\'t be empty')
                    except ValueError as err:
                        print ('Input error: {}'.format(err))
                        continue
                    else:
                        property_list['Serial'] = modified_serial
                        device_obj.configure_properties(ip_addr_key, **property_list)
                else:
                    print('You\'ve not made any choice for modifying device\'s properties. Device\'s properties are unchanged.')
                    continue
                print ('\tIP Address: {}'.format(ip_addr_key))
                device_obj.show_properties(ip_addr_key)
            else:
                print("Invalid response!")
                continue
            confirmation = input("Do you still want to retrieve device's properties? (y/n)")
            if confirmation.lower() == 'n' or confirmation.lower() == 'no':
                break
            elif confirmation.lower() == 'y' or confirmation.lower() == 'yes':
                continue
            else:
                try:
                    raise ValueError("Not a valid response!")
                except ValueError as err:
                    print ('Input error: {}'.format(err))
        else:
            print("The IP you've entered is not in the database.")
            device_obj.show_ip()

    device_obj.save_to_json()
except KeyboardInterrupt:
    print ("User aborted!")