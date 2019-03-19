import yaml
from ciscoconfparse import CiscoConfParse
from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

infile = input("Where is your device list:  ")

with open(infile) as f:
    device_list = yaml.load(f)
f.close()


device = device_list['cisco4']

net_connect = ConnectHandler(**device)
run_config = net_connect.send_command("show run")
net_connect.disconnect()

cisco_obj = CiscoConfParse(run_config.splitlines())

match  = cisco_obj.find_objects_w_child(parentspec=r"^interface", childspec="^\s+ip address")

interface = "Interface Line: " + match[0].text
ip_addr = "IP Address Line: " + match[0].children[0].text

print(interface)
print(ip_addr)




