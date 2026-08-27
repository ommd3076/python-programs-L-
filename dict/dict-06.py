status_codes = [200, 404, 200, 500, 200, 404]
counts = {}
for n in status_codes:
    if n in counts:
        counts[n] += 1
    else:
        counts[n] = 1
        
print(counts)