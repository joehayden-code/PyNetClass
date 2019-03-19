import yaml
from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

infile = input("Where is your device list:  ")

with open(infile) as f:
    device_list = yaml.load(f)

pprint(device_list)







