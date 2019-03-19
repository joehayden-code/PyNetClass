from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

def logstamp():

    lstamp = datetime.now()
    return str(lstamp.year) + '-' + str(lstamp.month) + '-' + str(lstamp.day) + '-' + str(lstamp.hour) + ':' + str(lstamp.minute) + ':' + str(lstamp.second)


device = {
       'host' : 'cisco3.lasthop.io',
       'username' : 'pyclass',
       'password' : getpass(),
       'device_type' : 'cisco_ios',
       'fast_cli': True
       }

print('**********')
print(logstamp())
print('**********')


net_connect = ConnectHandler(**device)

cfg = ['ip name-server 1.1.1.1',
       'ip name-server 1.0.0.1',
       'ip domain-lookup'
      ]

print(net_connect.find_prompt())

output = net_connect.send_config_set(cfg)


print('**********')
print(logstamp())
print('**********')

net_connect.disconnect()
print(output)






