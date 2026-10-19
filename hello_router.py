
# hello_router.py - my first Python script
hostname = "LON-CORE-01"
mgmt_ip = "10.10.10.1"
vlan_count = 12
is_up = False

print("Hello from", hostname)
print(f"{hostname} management IP is {mgmt_ip}")
print(f"It carries {vlan_count} VLANs. Up: {is_up}")


site = "Luton"

print(f"{hostname} is in {site}")
print(f"{hostname} at {site} is up: {is_up}")