def get_positives(nlist):
    l2 = []
    for n in nlist:
        if n > 0:
            l2.append(n)
    return l2

l1 = [-1,-2, 3, 4, -5, 6 ]
print(get_positives(l1))