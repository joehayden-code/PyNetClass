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

     #set log file name
     lstamp = datetime.now()
     logstamp = str(lstamp.year) + '-' + str(lstamp.month) + '-' + str(lstamp.day) + '-' + str(lstamp.hour) + str(lstamp.minute) + str(lstamp.second)
     logstamp = cxn['host'] + "-" + logstamp + '.log'
     cxn['session_log'] = logstamp

     #make connection
     net_connect = ConnectHandler(**cxn)
     print(net_connect.find_prompt())

     #if nxos2 then get version
     if "nxos2" in cxn['host']:
          output = net_connect.send_command("show version")
          print (output)

          with open('show_version.txt','w') as f:
               f.write(output)

     #disconnect
     net_connect.disconnect()



