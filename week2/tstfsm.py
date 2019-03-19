from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime
from pprint import pprint


def getStamp():
     lstamp = datetime.now()
     return str(lstamp.year) + '-' + str(lstamp.month) + '-' + str(lstamp.day) + '-' + str(lstamp.hour) + str(lstamp.minute) + str(lstamp.second)



cisco4 = {
       'host' : 'cisco4.lasthop.io',
       'username' : 'pyclass',
       'password' : getpass(),
       'device_type' : 'cisco_ios',
       'session_log' : 'cisco4-' + getStamp()
       }

net_connect = ConnectHandler(**cisco4)


#oShowVer = net_connect.send_command('show ver', use_textfsm=True)
#oShowLLDP = net_connect.send_command('show lldp nei', use_textfsm=True)

print()
cmds = ["show version", "show lldp neighbors"]
for cmd in cmds:
    output = net_connect.send_command(cmd, use_textfsm=True)
    print("#" * 80)
    print(cmd)
    print("#" * 80)
    pprint(output)
    print("#" * 80)
    print()

    if cmd == "show lldp neighbors":
        print("LLDP Data Structure Type: {}".format(type(output)))
        print("HPE Switch Connection Port: {}".format(output[0]["neighbor_interface"]))

print()




net_connect.disconnect()

