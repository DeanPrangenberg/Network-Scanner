# Netzwerk-Scanner

Dieses Python-Projekt scannt ein lokales Netzwerk und ermittelt die IP- und MAC-Adressen der verbundenen Geräte. Zusätzlich wird für jede MAC-Adresse der Hersteller (Vendor) mithilfe der `macvendors.com` API abgerufen.

## Funktionen

- **Netzwerkscan:** Sucht nach Geräten im angegebenen Subnetz und sammelt IP- und MAC-Adressen.
- **Vendor-Erkennung:** Ruft den Hersteller (Vendor) der Geräte anhand ihrer MAC-Adresse ab.
- **Übersichtliche Darstellung:** Zeigt die gefundenen Geräte in einer übersichtlichen Tabelle an.

## Installation

1. **Voraussetzungen:**
   - Python 3.x
   - `scapy` Bibliothek
   - `requests` Bibliothek
   - `prettytable` Bibliothek

2. **Installation der benötigten Pakete:**

   ```bash
   pip install scapy requests prettytable
   ```
3. **Installation von Npcap** (für Windows-Nutzer):

Scapy erfordert Npcap, um Netzwerkschnittstellen zu überwachen. Lade Npcap von der offiziellen Website herunter und installiere es.

## Verwendung
1. Ändere die Ziel-IP/Subnetz in der Datei main.py, um dein Netzwerk anzugeben (z.B. 192.168.1.1/24).

1. Führe das Skript mit Administratorrechten aus:

```bash
python main.py
```
3. Die gescannten Geräte und deren Informationen werden in einer Tabelle ausgegeben.

## Beispiel
```plaintext
+---------------+-------------------+----------------------+
| IP-Adresse    | MAC-Adresse       | Hersteller           |
+---------------+-------------------+----------------------+
| 192.168.1.2   | 00:1A:2B:3C:4D:5E | Apple, Inc.          |
| 192.168.1.3   | 00:1B:44:11:3A:B7 | Samsung Electronics  |
+---------------+-------------------+----------------------+
```
## Hinweis
Dieses Skript funktioniert nur korrekt, wenn es mit Administratorrechten ausgeführt wird, da es auf Netzwerkschnittstellen zugreifen muss.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
Email: prangenbergdean@gmail.com
