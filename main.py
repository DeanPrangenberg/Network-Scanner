import requests
from scapy.layers.l2 import ARP, Ether
from scapy.sendrecv import srp
import prettytable as pt
import socket

def network_scan(target_ip):
    # Create ARP request
    arp = ARP(pdst=target_ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")  # Broadcast to all devices
    packet = ether / arp

    # Send the packet and wait for responses
    result = srp(packet, timeout=2, verbose=False)[0]

    # Create a table for clear representation
    table = pt.PrettyTable(["IP Address", "MAC Address", "Manufacturer", "Device Name"])

    # Process the responses
    for sent, received in result:
        mac_address = received.hwsrc
        vendor = get_vendor(mac_address)  # Retrieve manufacturer by MAC address
        device_name = get_device_name(received.psrc)  # Get the device name via reverse DNS
        table.add_row([received.psrc, mac_address, vendor, device_name])

    print(table)

def get_vendor(mac_address):
    # Use the macvendors.co API to determine the manufacturer
    try:
        url = f"https://api.macvendors.com/{mac_address}"
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.text.strip()
        else:
            return "Unknown Manufacturer"
    except requests.RequestException:
        return "API Request Failed"

def get_device_name(ip_address):
    # Attempt to resolve the hostname from the IP address
    try:
        hostname, _, _ = socket.gethostbyaddr(ip_address)
        return hostname
    except socket.herror:
        return "Unknown Device"

if __name__ == "__main__":
    # Specify the network subnet (e.g., 192.168.178.1/24 for a typical home network)
    target_ip = "192.168.178.1/24"
    print(f"Scanning network: {target_ip}")
    network_scan(target_ip)
