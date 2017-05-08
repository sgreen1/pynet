#!/usr/bin/env python

import pexpect
import sys
from getpass import getpass

def main():
    ip_addr = '184.105.247.70'
    username = 'pyclass'
    password = '88newclass'
    port = 22

    ssh_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(username, ip_addr, port))
    ssh_conn.timeout = 3
    ssh_conn.expect('ssword:')
    ssh_conn.sendline(password)
    ssh_conn.expect('#')
    
    ssh_conn.sendline('terminal length 0')
    ssh_conn.expect('pynet-rtr1#')

    ssh_conn.sendline('sh ver')
    ssh_conn.expect('pynet-rtr1#')

    print ssh_conn.after
    print ssh_conn.before


if __name__ == "__main__":
    main()
