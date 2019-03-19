import yaml
from pprint import pprint

cisco3 = {"device_name":"cisco3", "hostname":"cisco3.lasthop.io"} 
cisco4 = {"device_name":"cisco4", "hostname":"cisco4.lasthop.io"} 
arista1 = {"device_name":"arista1", "hostname":"arista1.lasthop.io"} 
arista2 = {"device_name":"arista2", "hostname":"arista2.lasthop.io"} 
arista3 = {"device_name":"arista3", "hostname":"arista3.lasthop.io"} 
arista4 = {"device_name":"arista4", "hostname":"arista4.lasthop.io"} 
srx2 = {"device_name":"srx2", "hostname":"srx2.lasthop.io"} 
nxos1 = {"device_name":"nxos1", "hostname":"nxos1.lasthop.io"} 
nxos2 = {"device_name":"nxos2", "hostname":"nxos2.lasthop.io"}


my_devices = [cisco3, cisco4, arista1, arista2, arista3, arista4, srx2, nxos1, nxos2]

for device in my_devices:
    device["username"] = "admin"
    device["password"] = "123456"

print()
pprint(my_devices)
print()


with open("devices.yml", "w") as f:
    yaml.dump(my_devices, f, default_flow_style=False)


