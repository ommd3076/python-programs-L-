servers = [
    {"id": "srv-01", "region": "india"},
    {"id": "srv-02", "region": "germany"},
    {"id": "srv-03", "region": "india"},
    {"id": "srv-04", "region": "usa"},
    {"id": "srv-05", "region": "germany"},
]

region_map = {} 
for key,value in servers[0].items():
    if value == "india":
        region_map[key].append(value)
    elif value == "germany":
        region_map[key].append(value)
    elif value == "usa":
        region_map[key].append(value)
        
print(region_map)