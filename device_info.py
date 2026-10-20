# device_info.py - storing a device's details in a dictionary
device = {
    "hostname": "lon-core-01",
    "mgmt_ip": "10.10.10.1",
    "vendor": "cisco",
    "model": "C9300",
    "vlan_count": 12,
}

print(device)
print(device["hostname"])
print(device["vlan_count"])
print(f"{device['hostname']} is a {device['vendor']} {device['model']}")

device["vlan_count"] = 15

print(device)

device["site"] = "Luton"

print(device)

# Safe lookup
print(device.get("serial", "unknown"))
print(device.get("model", "unknown"))

# A router's interfaces as a dictionary
interfaces = {
    "Gi0/0": "up",
    "Gi0/1": "down",
    "Gi0/2": "admin down",
}

print(interfaces["Gi0/1"])
print(f"Gi0/2 is {interfaces['Gi0/2']}")
print(interfaces.get("Gi0/9", "no such interface"))
print(len(interfaces))

interfaces["Gi0/1"] = "up"
interfaces["Gi0/3"] = "down"

print(interfaces)
