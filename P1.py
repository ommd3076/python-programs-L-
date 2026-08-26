def addto10(n):
    n = [1, 4, 6, 3]
    for i in range(len(n)):
        for j in range(i+1, len(n)):
            if n[i] + n[j] == 10:
                return True
    return False
print(addto10(0))