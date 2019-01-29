#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

lstamp = datetime.now()
logstamp = str(lstamp.year) + '-' + str(lstamp.month) + '-' + str(lstamp.day) + '-' + str(lstamp.hour) + str(lstamp.minute) + str(lstamp.second)

net_connect = ConnectHandler(
     host='nxos1.lasthop.io',
     username='pyclass',
     password=getpass(),
     device_type='cisco_nxos',
     session_log='nxos1-' + logstamp + ".txt"
)

print(net_connect.find_prompt())

