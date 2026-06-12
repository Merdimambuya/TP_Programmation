table_arp = {
    "192.168.100.1": "AA:BB:CC:DD:EE:FF",
    "192.168.100.20": "11:22:33:44:55:66",
    "192.168.100.10": "77:88:99:AA:BB:CC"
}

print("=== Table ARP ===")

for ip, mac in table_arp.items():
    print(f"{ip:<15} {mac}")