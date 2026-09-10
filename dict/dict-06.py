status_codes = [200, 404, 200, 500, 200, 404]
counts = {}
for n in status_codes:
    counts[n] = counts.get(n, 0) + 1
        
print(counts)