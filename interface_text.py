# interface_text.py - working with text from network devices

interface = "GigabitEthernet0/1"
mgmt_ip = "192.168.50.7"
hostname = "lon-core-01"

# 1. change case
print(hostname.upper())

# 2. Count characters
print(len(interface))

# 3. Check what something starts with
print(interface.startswith("Gig"))

# 4. Split an IP into its four octets
octets = mgmt_ip.split(".")
print(octets)
print(f"First octet is {octets[0]} and last octet is {octets[3]}")