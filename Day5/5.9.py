"""
Write a python program to check valid IPV4 and IPV6 ip address (Regex) 

"""

import re


def check_valid_ip(ip_address):
    ipv4_pattern = r"^(\d{1,3}\.){3}\d{1,3}$"
    ipv6_pattern = r"^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$"

    if re.match(ipv4_pattern, ip_address):
        return "Valid IPv4 address"
    elif re.match(ipv6_pattern, ip_address):
        return "Valid IPv6 address"
    else:
        raise ValueError("Invalid IP address")


# Example usage
try:
    ip_address = input("Enter an IP address: ")
    result = check_valid_ip(ip_address)
    print(result)
except ValueError as err:
    print(str(err))

"""
Input1: Enter an IP address: 192.168.0.1
Output1: Valid IPv4 address

Input2: Enter an IP address: 2001:0db8:85a3:0000:0000:8a2e:0370:7334
Output2: Valid IPv6 address

Input3: Enter an IP address: 10.0.0
Output3: Invalid IP address

Input4: Enter an IP address: 192.168.0.300
Ouptput4: Invalid IP address

"""
