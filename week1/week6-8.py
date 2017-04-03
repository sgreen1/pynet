#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse

def main():

    ciscocfg = CiscoConfParse("cisco_ipsec.txt")

    crypto_map = ciscocfg.find_objects(r"^crypto map CRYPTO")

    for c_map in crypto_map:
        print
        print c_map.text
        for child in c_map.children:
            print child.text 

    print

if __name__ == '__main__':
    main()
       
   
