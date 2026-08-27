server_loads = {"web": 45, "db": 92, "cache": 15}
for server, load in server_loads.items():
    if load > 90:
        print(server)
