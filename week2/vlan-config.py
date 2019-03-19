from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

def logstamp():

    lstamp = datetime.now()
    return str(lstamp.year) + '-' + str(lstamp.month) + '-' + str(lstamp.day) + '-' + str(lstamp.hour) + '-' + str(lstamp.minute) + '-' + str(lstamp.second)

uid = 'pyclass'
pwd = getpass()
dev = 'cisco_nxos'

devices = ['nxos1.lasthop.io','nxos2.lasthop.io']


for device in devices:
     
     net_connect = ConnectHandler(host=device,
                                  username = uid,
                                  password = pwd,
                                  device_type = dev,
                                  session_log = device + logstamp() + '.txt'
                                 )


     net_connect.send_config_from_file(config_file='vlan-cfg.txt')
     net_connect.save_config()
     print(device.upper() + ' configuration complete!')


net_connect.disconnect()


