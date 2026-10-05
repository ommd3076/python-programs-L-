
reports = [
    ("server_1", "asia"),
    ("server_2", "europe"),
    ("server_3", "asia"),
    ("server_4", "america"),
    ("server_5", "europe"),
    ("server_6", "asia")
]

region_map = {}

for server_id, region in reports:
    if region in region_map:
        region_map[region] = []
    
region_map[region].append(server_id)

print(region_map)