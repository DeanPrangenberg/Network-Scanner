import requests
from scapy.layers.l2 import ARP, Ether
from scapy.sendrecv import srp
import prettytable as pt

def network_scan(target_ip):
    # Erstelle ARP Anfrage
    arp = ARP(pdst=target_ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")  # Broadcast an alle Geräte
    packet = ether / arp

    # Sende das Paket und warte auf Antworten
    result = srp(packet, timeout=2, verbose=False)[0]

    # Erstelle eine Tabelle für eine übersichtliche Darstellung
    table = pt.PrettyTable(["IP-Adresse", "MAC-Adresse", "Hersteller"])

    # Verarbeite die Antworten
    for sent, received in result:
        mac_address = received.hwsrc
        vendor = get_vendor(mac_address)  # Hersteller über die MAC-Adresse abrufen
        table.add_row([received.psrc, mac_address, vendor])

    print(table)

def get_vendor(mac_address):
    # Verwende die API von macvendors.co, um den Hersteller zu ermitteln
    try:
        url = f"https://api.macvendors.com/{mac_address}"
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.text.strip()
        else:
            return "Unbekannter Hersteller"
    except requests.RequestException:
        return "API-Anfrage fehlgeschlagen"

if __name__ == "__main__":
    # Netzwerksubnetz angeben (zum Beispiel 192.168.178.1/24 für ein typisches Heimnetzwerk)
    target_ip = "192.168.178.1/24"
    print(f"Scanning Netzwerk: {target_ip}")
    network_scan(target_ip)
