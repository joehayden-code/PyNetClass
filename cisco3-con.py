#!/usr/bin/env python

from datetime import date, time, datetime
from netmiko import ConnectHandler
from getpass import getpass

logtime = str(datetime.now())

net_connect = ConnectHandler(host='cisco3.lasthop.io',
                             username='pyclass',
                             password=getpass(),
                             device_type='cisco_ios',
                             session_log='cisco.log')

print (net_connect.find_prompt())

