#!/usr/bin/env python

import pexpect
import sys
from getpass import getpass

def main():
    ip_addr = '184.105.247.70'
    username = 'pyclass'
    password = getpass()
    port = 22

    ssh_conn = pexpect.spawn('ssh -l {} {}'.format(username, ip_addr))

    ssh_conn.timeout = 3
    ssh_conn.expect('ssword:')
    ssh_conn.sendline(password)

    ssh_conn.expect('#')
    print ssh_conn.before
    print ssh_conn.after


if __name__ == "__main__":
    main()
