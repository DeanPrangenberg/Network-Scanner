
# Network Scanner

This Python project scans a local network and retrieves the IP and MAC addresses of connected devices. Additionally, for each MAC address, the manufacturer (vendor) is fetched using the `macvendors.com` API.

## Features

- **Network Scan:** Searches for devices in the specified subnet and collects their IP and MAC addresses.
- **Vendor Lookup:** Fetches the manufacturer (vendor) of devices based on their MAC address.
- **Clear Display:** Shows the found devices in a well-organized table.

## Installation

1. **Requirements:**
   - Python 3.x
   - `scapy` library
   - `requests` library
   - `prettytable` library

2. **Install required packages:**

   ```bash
   pip install scapy requests prettytable
   ```

3. **Install Npcap** (for Windows users):

   Scapy requires Npcap to monitor network interfaces. Download and install Npcap from the [official website](https://nmap.org/npcap/).

## Usage

1. Change the target IP/subnet in the `main.py` file to match your network (e.g., `192.168.1.1/24`).

2. Run the script with administrator privileges:

   ```bash
   python main.py
   ```

3. The scanned devices and their information will be displayed in a table.

## Example

```plaintext
+---------------+-------------------+----------------------+
| IP Address    | MAC Address       | Vendor               |
+---------------+-------------------+----------------------+
| 192.168.1.2   | 00:1A:2B:3C:4D:5E | Apple, Inc.          |
| 192.168.1.3   | 00:1B:44:11:3A:B7 | Samsung Electronics  |
+---------------+-------------------+----------------------+
```

## Note
This script only works correctly if run with administrator privileges, as it needs access to network interfaces.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
Email: prangenbergdean@gmail.com
