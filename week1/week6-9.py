#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse
from pprint import pprint as pp

def main():
    ciscocfg = CiscoConfParse("cisco_ipsec.txt")

    crypto_maps = ciscocfg.find_objects_w_child(parentspec=r'crypto map CRYPTO',childspec=r'pfs group2')

    print("Crypto maps using PFS Group 2:\n")
    for line in crypto_maps:
        print line.text


if __name__ == '__main__':
    main()
