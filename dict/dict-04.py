# This program creates a list of active server IDs from a list of server dictionaries.
servers = [{"id": 1, "state": "up"}, {"id": 2, "state": "down"}, {"id": 3, "state": "up"}]
active_ids = []
for s in servers:
    if s["state"] == "up":
        active_ids.append(s["id"])
print(active_ids)

