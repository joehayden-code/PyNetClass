import json
from pprint import pprint

infile = "nxos-intf.json"
ipv4_addr = []
ipv6_addr = []

with open(infile) as f:
    data = json.load(f)

pprint(data)
print("#" * 80)
print()

for intf, if_config in data.items():

    for addr_type, addr in if_config.items():

        if addr_type == "ipv4":
            for key in addr:
                ipv4_addr.append(key)
        else:
            for key in addr:
                ipv6_addr.append(key)

print("IPv4 Addresses")
pprint (ipv4_addr)
print()
print("IPv6 Addresses")
pprint (ipv6_addr)
print()



