#!/usr/bin/env python

import telnetlib
from pprint import pprint as pp
import time

TELNET_PORT = 23
TELNET_TIMEOUT = 6


def login(remote_conn, username, password):
    output = remote_conn.read_until("sername:", TELNET_TIMEOUT)
    remote_conn.write(username + '\n')
    output += remote_conn.read_until("assword:", TELNET_TIMEOUT)
    remote_conn.write(password + '\n')
    return output

def send_command(remote_conn, cmd):
    cmd = cmd.rstrip()
    remote_conn.write(cmd + '\n')
    time.sleep(1)
    return remote_conn.read_very_eager()
   

def main():
    ip_addr = '184.105.247.70'
    username = 'pyclass'
    password = '88newclass' 

    remote_conn = telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)

    output = login(remote_conn, username, password)

    print("doing stuff and thangs\n")
    
    output = send_command(remote_conn, 'terminal length 0')
    arp_output = send_command(remote_conn, 'show ip arp')

    config_output = send_command(remote_conn, 'show config')

    output = remote_conn.read_very_eager()

    print output
    #print config
    #print(config)
 
    f = open("config.txt", 'w')
    f.write(config_output)
    f.close()
    f = open("arp.txt", 'w')
    f.write(arp_output)
    f.close()


   


main()



