# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 21:17:36 2016

@author: Zeyi
"""

import socket
import ipaddress

def is_valid_ipv4_address(address):
    try:
        socket.inet_pton(socket.AF_INET, address)
    except AttributeError:  # no inet_pton here, sorry
        try:
            socket.inet_aton(address)
        except socket.error:
            return False
        return address.count('.') == 3
    except socket.error:  # not a valid address
        return False

    return address.count('.') == 3

def is_valid_ipv6_address(address):
    try:
        socket.inet_pton(socket.AF_INET6, address)
    except socket.error:  # not a valid address
        return False
    return True

def create_network_maskset(network_list):
     """
     Takes in a iterable of strings respresenting network masks
     e.g. "192.168.0.0/22"
     return mask_set
     """
     #Transform to unicode as ipaddress module can only work with that
     mask_list = [ipaddress.ip_network(IPs.decode('utf-8')) for IPs in network_list]
     mask = frozenset(mask_list) #Optional
     return mask

if __name__ == "__main__":
     #Demo of ip in network subnet check   
     
     #Map IP to ipaddress object first
     #Step 1: decode all IPs to unicode
     #df['c_ip'].str.decode('utf-8')
     #c_ip_mapped = df['c_ip'].map(lambda x:ipaddress.ip_address(x))
     
     #Check if in subnet list
     #subnetlist = ['192.168.0.0/22','134.132.4.56/23', ...]
     #subnets = create_network_maskset(subnetlist)
     #to_remove = c_ip_mapped.map(lambda x: any(x in net for net in subnets))
     
     #Filter
     #df = df[to_remove == False]
     
     #return df