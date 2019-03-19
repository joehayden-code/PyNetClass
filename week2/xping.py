from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

lstamp = datetime.now()
logstamp = str(lstamp.year) + '-' + str(lstamp.month) + '-' + str(lstamp.day) + '-' + str(lstamp.hour) + str(lstamp.minute) + str(lstamp.second)



cisco4 = {
       'host' : 'cisco4.lasthop.io',
       'username' : 'pyclass',
       'password' : getpass(),
       'device_type' : 'cisco_ios',
       'session_log' : 'cisco4-' + logstamp
       }


net_connect = ConnectHandler(**cisco4)

output = net_connect.send_command('ping', expect_string=r'ip')
output = net_connect.send_command('\n', expect_string=r'address')
output += net_connect.send_command('8.8.8.8', expect_string=r'count')
output += net_connect.send_command('5', expect_string=r'size')
output += net_connect.send_command('100',expect_string=r'seconds')
output += net_connect.send_command('2',expect_string=r'commands')
output += net_connect.send_command('n',expect_string=r'sizes')
output += net_connect.send_command('n',expect_string=r'#')

net_connect.disconnect()
print(output)






