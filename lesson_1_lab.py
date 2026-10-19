hostname = "man-dis-02"
mgmt_ip = "172.16.4.25"

print(f"{hostname.upper()} manages {mgmt_ip}")

octets = mgmt_ip.split(".")
print(octets)
print(f"This ip starts with {octets[0]}")
print(f"The 3rd octet is {octets[2]}")

print(f"The octet with -1 {octets[-1]}")