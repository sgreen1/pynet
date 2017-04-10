#!/usr/bin/env python

import telnetlib
from pprint import pprint as pp
import time

TELNET_PORT = 23
TELNET_TIMEOUT = 6


def send_command(remote_conn, cmd):
    cmd = cmd.rstrip()
    remote_conn.write(cmd + '\n')
    time.sleep(1)
    return remote_conn.read_very_eager()
   

def telnet_connect():
    ip_addr = '184.105.247.70'
    username = 'pyclass'
    password = '88newclass' 

    remote_conn = telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
    
    output = remote_conn.read_until("sername:", TELNET_TIMEOUT) 

    output = send_command(remote_conn, username)

    output = remote_conn.read_until("assword:", TELNET_TIMEOUT)

    output = send_command(remote_conn, password) 

    output = send_command(remote_conn, 'terminal length 0')
    arp_output = send_command(remote_conn, 'show ip arp')

    config_output = send_command(remote_conn, 'show config')

    output = remote_conn.read_very_eager()

    #print output
    #print config
    #print(config)
 
    f = open("config.txt", 'w')
    f.write(config_output)
    f.close()
    f = open("arp.txt", 'w')
    f.write(arp_output)
    f.close()


   


telnet_connect()



