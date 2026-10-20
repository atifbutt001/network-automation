#dictionary lab after lesson 2
vlans = {
    10: "Users",
    20: "Voice",
    99: "Management",
}

print(vlans [99])

vlans[20] = "VoIP"

vlans[30] = "Printers"

print(vlans.get(50, "not configured"))
print(len(vlans))
print(vlans)