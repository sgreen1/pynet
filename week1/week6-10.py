#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse

from pprint import pprint as pp

ciscocfg = CiscoConfParse("cisco_ipsec.txt")

transform_sets = ciscocfg.find_objects_w_child(parentspec=r'crypto map CRYPTO', childspec='3DES')

print("The following crypto maps are not using AES:\n")

for line in transform_sets:
    print line.text
