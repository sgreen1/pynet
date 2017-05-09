#!/usr/bin/env python

import sys
import time
import paramiko

MAX_BUFFER = 65365

def clear_buffer(remote_conn):
    ''' 
    Clear data from the receive buffer.
    '''
    if remote_conn.recv_ready():
        return remote_conn.recv(MAX_BUFFER)


def disable_paging(remote_conn, cmd='terminal length 0'):
    '''
    Disable terminal paging
    '''
    cmd = cmd.strip()
    remote_conn.send(cmd + '\n')
    time.sleep(1)
    clear_buffer(remote_conn)

def send_command(remote_conn, cmd='', delay=1):
    ''' 
    Sencd command down the channel. Retreive and return the output.
    '''
    if cmd != '':
        cmd = cmd.strip()
    remote_conn.send(cmd + '\n')
    time.sleep(delay)

    if remote_conn.recv_ready():
        return remote_conn.recv(MAX_BUFFER)
    else:
        return ''

def main():
    '''
    Main business here.
    '''
    
    ip_addr = '184.105.247.70'
    username = 'pyclass'
    password = '88newclass'
    port = 22
    
    remote_conn_pre = paramiko.SSHClient()
    remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    remote_conn_pre.connect(ip_addr, username=username, password=password, look_for_keys=False, allow_agent=False)

    remote_conn = remote_conn_pre.invoke_shell()

    clear_buffer(remote_conn)
    disable_paging(remote_conn)

    send_command(remote_conn, cmd='config t')
    send_command(remote_conn, cmd='logging buffered 6666')
    send_command(remote_conn, cmd='end')
    
    output = send_command(remote_conn, cmd='sh run | include logging')
    
    print output
    


    print output


if __name__ == "__main__":
    main()
