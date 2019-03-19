import json
from pprint import pprint

infile = "arista-arp.json"
arp_table = {}
index = 0

with open(infile) as f:
    data = json.load(f)

for entries, neighbors in data.items():

    if entries == "ipV4Neighbors":
        
        for index in range(len(neighbors)):
            for key in neighbors[index]:
                if key == "hwAddress":
                    mac = neighbors[index][key]
                if key == "address":
                    arp_table[neighbors[index][key]] = mac

print(arp_table)




#Easier Way
#arp_dict = {}
#arp_entries = arp_data["ipV4Neighbors"]
#for entry in arp_entries:
#    ip_addr = entry["address"]
#    mac_addr = entry["hwAddress"]
#    arp_dict[ip_addr] = mac_addr


