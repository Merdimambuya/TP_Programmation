dns_records = {
    "google.com": "142.250.74.14",
    "github.com": "140.82.121.4",
    "openai.com": "104.18.33.45"
}

print("=== Analyse DNS ===")

for domaine, ip in dns_records.items():
    print(f"{domaine} -> {ip}")