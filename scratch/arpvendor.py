#!/usr/bin/env python

from pprint import pprint as pp

def get_arps(arpfile):
    arps = {}
    for line in arpfile:
        if 'Internet' in line:
            arps[line.split()[3]] = line.split()[5]
    return arps
#def reformat_macs(arps):
    

def main():
    f = open("arp.txt", 'r')

    output = get_arps(f)
    pp(output)


if __name__ == "__main__":
    main()
