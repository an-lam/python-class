# read_config.py
"""
Make sure pyyaml is installed:
c:> pip install pyyaml
"""
import yaml

raspberry_config = "config_file"

if __name__ == '__main__':
    with open(raspberry_config, 'r') as ymlfile:
        cfg = yaml.load(ymlfile)

    print("Sections in config file:")
    for section in cfg:
        print(section)
        #print(cfg[section]['host'])

    print("mydevice0: {}".format(cfg['mydevice0']))
    print("mydevice1.host: " + cfg['mydevice1']['host'])
    print("log: {}".format(cfg['log']))

