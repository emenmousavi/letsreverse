import socket
import ipinfo
from colorama import Fore, Style

def get_reverse_dns(ip_address):
    try:
        hostnames = socket.gethostbyaddr(ip_address)
        return hostnames[0]
    except socket.herror:
        return "Reverse DNS not found"

def get_ip_information(ip_address):
    access_token = '35d39df4e68fec'
    handler = ipinfo.getHandler(access_token)
    details = handler.getDetails(ip_address)
    
    is_private_ip = ip_address.startswith(('10.', '172.', '192.168.'))
    
    return {
        'ISP': details.org,
        'Country': details.country_name,
        'Region': details.region,
        'Private IP': is_private_ip
    }

def main():
    ip_address = input("Enter an IPv4 or IPv6 address: ")

    reverse_dns = get_reverse_dns(ip_address)
    print(f"{Fore.CYAN}Reverse DNS:{Style.RESET_ALL} {reverse_dns}")

    ip_info = get_ip_information(ip_address)
    print(f"{Fore.MAGENTA}ISP:{Style.RESET_ALL} {ip_info['ISP']}")
    print(f"{Fore.CYAN}Country:{Style.RESET_ALL} {ip_info['Country']}")
    print(f"{Fore.MAGENTA}Region:{Style.RESET_ALL} {ip_info['Region']}")
    print(f"{Fore.CYAN}Is it private IP?:{Style.RESET_ALL} {ip_info['Private IP']}")

if __name__ == "__main__":
    main()
