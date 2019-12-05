def is_correct_structure(ip_address):
    items = ip_address.split('.')
    if len(items) != 4:
        return False
    return True

def is_part_in_range(part):
    if 0 <= int(part) <= 255:
        return True
    return False

def is_part_only_digits(part):
    if part.isdigit():
        return True
    return False

def is_four_zeros(ip_address):
    if ip_address == '0.0.0.0':
        return True
    return False

def check_parts(ip_address):
    parts = ip_address.split('.')
    name_parts = [('first', parts[0]), ('second', parts[1]), ('third', parts[2]), ('fourth', parts[3])]

    for item in name_parts:
        if not is_part_only_digits(item[1]):
            print("Not a valid IP address." +
                  " The {0} part of the IP ({1}) must only have digits\n".format(item[0], item[1]))
            return False

        if not is_part_in_range(item[1]):
            print("Not a valid IP address. " +
                  "The {0} part of the IP ({1}) must be between 0-255\n".format(item[0], item[1]))
            return False

    return True



def validate_ip_address(ip_address):

    if not is_correct_structure(ip_address):
        print("Not a valid IP address, IP must have form of ###.###.###.###")
        print("The IP address that you entered {} is missing a . \n".format(ip_address))
        return False

    if is_four_zeros(ip_address):
        print("Not a valid IP address. IP address can not be all zeros\n")
        return False

    if check_parts(ip_address):
        print('Ping {}'.format(ip_address))
        return True


def is_IP_in_DB(ip_address, devices):
    return ip_address in list(devices.keys())

def IP_not_found(ip_address, devices):
    ip_list = list(devices.keys())
    count = 1
    print("That IP address is not in our database. The avalible IP addresses are:")
    for ip in ip_list:
        if count % 4 != 0:
            print(ip, end='; ')
            count += 1
        else:
            print(ip)
            count += 1

def print_device_properties(ip_address, device):
    print("The Device at address {} has the following properties: ".format(ip_address))
    print("Location: {}".format(device.get('location')))
    print("Model: {}".format(device.get('model')))
    print("Serial: {}".format(device.get('serial_number')))

def create_device():
    print("Enter a Location: ")
    location = input()
    print("Enter Model: ")
    model = input()
    print("Enter Serial number: ")
    serial_number = input()
    device = {'location': location, 'model': model, 'serial_number': serial_number}
    return device

def change_device_properties(device):
    while True:
        print("What property would you like to change? ")
        prop = input()
        if not is_valid_property(prop, device):
            show_valid_properties(prop, device)
            continue
        print("What would you like to change the {} to be?: ".format(prop))
        prop_value = input()
        device[prop] = prop_value

        if would_like_to_change_another_prop():
            continue
        else:
            break


def would_like_to_make_change_to_device():
    while True:
        print("Would you like to make change to this device? (Yes or No): ")
        answer = input()
        if is_yes_or_no(answer):
            return is_yes(answer)
        else:
            print("Sorry I did not understand, the answer should be Yes or No.")

def would_like_to_change_another_prop():
    while True:
        print("Would you like to make another change? (Yes or No): ")
        answer = input()
        if is_yes_or_no(answer):
            return is_yes(answer)
        else:
            print("Sorry I did not understand, the answer should be Yes or No")

def is_yes(answer):
    return answer == 'Yes' or answer == 'yes'

def is_yes_or_no(answer):
    correct_answers = ['Yes', 'yes', 'No', 'no']
    return answer in correct_answers



def is_valid_property(prop, device):
    return prop in list(device.keys())

def show_valid_properties(prop, device):
    print("Sorry but this device dose not have the propety {}. The avalible properties are: ".format(prop))
    for prop in list(device.keys()):
        print(prop, end=', ')


if __name__ == "__main__":
    ip = "9.1.88.9"
    #ip = ""
    good = validate_ip_address(ip)
    print(good)


