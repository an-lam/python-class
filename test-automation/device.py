import simplejson as json
class Device(object):

    def __init__(self):
        self._status = "False"
        self._exist = "True"
        self.__device_info = {}

    def validate_ip_addr(self, ip_addr):
        self._ip_addr = ip_addr
        octet_list = []
        octet_list = self._ip_addr.split('.')
        if len(octet_list) != 4:
            print ('IP address {} was not in correct format'.format(self._ip_addr))
            return self._status
        if self._ip_addr == "0.0.0.0":
            print ('IP adress {} is not a valid ip address!'.format(self._ip_addr))
            return self._status
        else:
            for octet in octet_list:
                try:
                    if len(octet) > 3 or len(octet) < 1:
                        raise ValueError('Octet length should be between 1 and 3')
                    elif not octet.isdigit():
                        raise ValueError('Octet {} is not a digit!'.format(octet))
                    else:
                        if 0 > int(octet) or int(octet) > 255:
                            raise ValueError('Octet {} you\'ve entered is out of range'.format(int(octet)))
                except ValueError as err:
                    print ('Error: {}'.format(err))
                    return self._status
            return self._status == "True"

    def check_ip_in_database(self, ip_addr):
        self._ip_addr = ip_addr
        if self._ip_addr in self.__device_info:
            print ('Found IP address {} in database'.format(self._ip_addr))
            return self._exist
        else:
            return self._exist == "False"

    def show_ip(self):
        print('List of IP Address(s) you\'ve entered so far')
        for _key in self.__device_info:
            print(_key)

    def configure_properties(self, ip_addr, **kwargs):
        self._ip_addr = ip_addr
        self.__device_info[self._ip_addr] = kwargs
        for _item, _value in kwargs.items():
            if _item == "Location":
                self.__device_info[self._ip_addr][_item] = _value
            elif _item == "Model":
                self.__device_info[self._ip_addr][_item] = _value
            elif _item == "Serial":
                self.__device_info[self._ip_addr][_item] = _value

    def show_properties(self, ip_addr):
        self._ip_addr = ip_addr
        for _item, _value in self.__device_info[self._ip_addr].items():
            print ('\t|___' +  _item + ': %s' % _value)

    def save_to_json(self):
        print("Writing dictionary to configuration databse ...")
        with open('./config.json', 'w') as json_file:
            json.dump(self.__device_info, json_file, indent=2)

if __name__ == "__name__":
    pass
