region_map = {}

region = "asia"
server_id = "server_1"
if region in region_map:
    key = region_map[region]
else:
    region_map[region] = []
region_map[region].append(server_id)
server_id = "server_2"
region_map[region].append(server_id)

print(region_map)