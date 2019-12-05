import os
import yaml

conf_file = "sample_config"
rasberry_config = "rasberry_config"

class YamlToDict():

    def __init__(self, config_file_name):
        self.yamlfile = config_file_name

    def yaml_to_dict(self):
        """
        read a YAML config file and converts to dictionary
        :return: a dictionary with tree data from YAML file
        """
        if self.yamlfile and os.path.isfile(self.yamlfile):
            try:
                with open(self.yamlfile) as config_file:
                    config_dict = yaml.load(config_file)
                    return config_dict
            except FileNotFoundError  as e:
                print("Config file not found: " + e)
        else:
            return None

if __name__ == '__main__':

    config_dict = YamlToDict(conf_file)
    params = config_dict.yaml_to_dict()

    for key in params.keys():
        print("config item: {}".format(key))
        print(params[key])

    with open(rasberry_config, 'r') as ymlfile:
        cfg = yaml.load(ymlfile)

    for section in cfg:
        print(section)

    print(cfg['address'])
    print(cfg['address']['ip'])

    print(cfg['login'])

