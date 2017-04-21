#!/usr/bin/env python


from pprint import pprint as pp
import yaml
import json 

def mac_reformat(macaddress):
    newmac = (macaddress[0] + macaddress[1] + ":" + macaddress[2] + macaddress[3] + ":" + macaddress[5] + macaddress[6]).upper()
    return newmac

def get_vendor(macaddr):
    for line in open("manuf.txt", 'r'):
        if mac_reformat(macaddr) in line:
            vendor = (' ').join(line.split()[3:])
            return vendor

arps = {line.split()[1]: [line.split()[3], line.split()[5], get_vendor(line.split()[3])] for line in open("arp.txt", 'r') if 'Internet' in line}

with open('arps_remaining.txt', 'w') as f:
    yaml.dump(arps)

print(yaml.dump(arps))
output = file('remaining_arps.yml', 'w')
yaml.dump(arps, output)


with open('remaining_arps.json', 'w') as f:
    json.dump(arps, f)

