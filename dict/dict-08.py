# This program groups server IDs by their region from a list of server dictionaries.
servers = [
    {"id": "srv-01", "region": "india"},
    {"id": "srv-02", "region": "germany"},
    {"id": "srv-03", "region": "india"},
    {"id": "srv-04", "region": "usa"},
    {"id": "srv-05", "region": "germany"},
]

region_map = {}

for server in servers:
    region = server["region"]
    server_id = server["id"]
    region_map.setdefault(region, []).append(server_id)

print(region_map)