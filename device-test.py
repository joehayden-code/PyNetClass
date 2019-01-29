#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

logstamp = ""

nxos1 = {
     "host":'nxos1.lasthop.io',
     "username":'pyclass',
     "password":getpass(),
     "device_type":'cisco_nxos',
     "session_log": logstamp
}

nxos2 = {
     "host":'nxos2.lasthop.io',
     "username":'pyclass',
     "password":getpass(),
     "device_type":'cisco_nxos',
     "session_log": logstamp
}

deviceList = [nxos1, nxos2]

for cxn in deviceList:

     lstamp = datetime.now()
     logstamp = str(lstamp.year) + '-' + str(lstamp.month) + '-' + str(lstamp.day) + '-' + str(lstamp.hour) + str(lstamp.minute) + str(lstamp.second)
     logstamp = cxn['host'] + "-" + logstamp + '.log'
     print(logstamp)
     cxn['session_log'] = logstamp

     net_connect = ConnectHandler(**cxn)
     print(net_connect.find_prompt())

