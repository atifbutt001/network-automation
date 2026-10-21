# loops.py - doing the same thing for each item
interfaces = ["Gi0/0", "Gi0/1", "Gi0/2", "Gi0/3"]

for name in interfaces:
    print(f"Checking {name}")

print("Done")

statuses = {
    "Gi0/0": "up",
    "Gi0/1": "down",
    "Gi0/2": "admin down",

}

for name in statuses:
    print(f"{name} is {statuses[name]}")