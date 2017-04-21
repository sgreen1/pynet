#!/usr/bin/env python

import sys
import time
import telnetlib
import getpass
import socket

TELNET_PORT = 23
TELNET_TIMEOUT = 6

def send_command(remote_conn, cmd):
    cmd = cmd.rstrip()
    remote_conn.write(cmd + '\n')
    time.sleep(1)
    return remote_conn.read_very_eager()

def telnet_connect(ip_addr):
    try:
        return telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
    except socket.timeout:
        sys.exit("Connection timed out.")

def disable_paging(remote_conn, paging_cmd='terminal length 0'):
    return send_command(remote_conn, paging_cmd)

def login(remote_conn, username, password):
    output = remote_conn.read_until("sername:", TELNET_TIMEOUT)
    remote_conn.write(username + '\n')
    output += remote_conn.read_until("assword:", TELNET_TIMEOUT)
    remote_conn.write(password + '\n')
    return output

def main():
    ip_addr = '184.105.247.70'
    username = 'pyclass'
    password = '88newclass'

    remote_conn = telnet_connect(ip_addr)
  
    output = login(remote_conn, username, password)

    time.sleep(1)
    remote_conn.read_very_eager()
    
    disable_paging(remote_conn)

    int_output = send_command(remote_conn, 'sh ip int brief')
    arp_output = send_command(remote_conn, 'sh arp')
    


    print("\n\n")
    print(intintintintintintintintintintintintintintintintintintintintintintintintintintintintint_____________________________output)
    print("\n\n")
    print(arp_output)


    remote_conn.close()

if __name__ == "__main__":
    main()


     
