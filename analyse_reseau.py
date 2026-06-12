from datetime import datetime

evenements = [
    ("TCP", "192.168.100.20", "192.168.100.1"),
    ("UDP", "192.168.100.20", "8.8.8.8"),
    ("ICMP", "192.168.100.20", "192.168.100.1")
]

print("=== Analyse Réseau ===")

for protocole, source, destination in evenements:
    print(
        f"[{datetime.now()}] "
        f"{protocole} | {source} -> {destination}"
    )