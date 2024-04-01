import socket
import ipinfo
from colorama import Fore, Style
from tabulate import tabulate

def get_reverse_dns(ip_address):
    try:
        hostnames = socket.gethostbyaddr(ip_address)
        return hostnames[0]
    except socket.herror:
        return "Reverse DNS not found"

def get_ip_information(ip_address, access_token):
    handler = ipinfo.getHandler(access_token)
    details = handler.getDetails(ip_address)
    
    is_private_ip = is_private(ip_address)
    
    return {
        'Reverse DNS': get_reverse_dns(ip_address),
        'ISP': details.org,
        'Country': details.country_name,
        'Region': details.region,
        'Is it private IP?': is_private_ip
    }

def is_private(ip_address):
    if ":" in ip_address:
        return False
    parts = ip_address.split(".")
    first_part = int(parts[0])
    
    if first_part == 10:
        return True
    elif first_part == 172 and 16 <= int(parts[1]) <= 31:
        return True
    elif first_part == 192 and int(parts[1]) == 168:
        return True
    else:
        return False
    
def main():
    access_token = input("Please enter your IPinfo API access token: ")
    ip_address = input("Enter an IPv4 or IPv6 address: ")

    ip_info = get_ip_information(ip_address, access_token)
    table_data = []
    for key, value in ip_info.items():
        table_data.append([key, value])

    print(tabulate(table_data, headers=["Attribute", "Value"]))

if __name__ == "__main__":
    main()
