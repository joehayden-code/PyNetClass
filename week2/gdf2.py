from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime


def logstamp():

     lstamp = datetime.now()
     return str(lstamp.year) + '-' + str(lstamp.month) + '-' + str(lstamp.day) + '-' + str(lstamp.hour) + str(lstamp.minute) + str(lstamp.second)


nxos2 = {
       'host' : 'nxos2.lasthop.io',
       'username' : 'pyclass',
       'password' : getpass(),
       'device_type' : 'cisco_nxos',
       'session_log' : 'nxos2-' + logstamp(),
       'global_delay_factor' : 8
       }

net_connect = ConnectHandler(**nxos2)

startStamp = logstamp()
print(startStamp)

output = net_connect.send_command("show lldp neighbors")
net_connect.disconnect()
print(output)


endStamp = logstamp()
print(endStamp)







