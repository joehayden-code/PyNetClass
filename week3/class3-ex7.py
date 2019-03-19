import yaml
import re
from ciscoconfparse import CiscoConfParse
from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

infile = input("Where is your device list:  ")

bgp_config = """
router bgp 44
 bgp router-id 10.220.88.38
 address-family ipv4 unicast
 !
 neighbor 10.220.88.20
  remote-as 42
  description pynet-rtr1
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
  !
 !
 neighbor 10.220.88.32
  remote-as 43
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
"""

cisco_obj = CiscoConfParse(bgp_config.splitlines())

match_nei = cisco_obj.find_objects_w_child(parentspec=r"^router bgp", childspec=r"^neighbor")





