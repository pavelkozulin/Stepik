a = [x for x in input().split()]
b = []
for i in a:
    if a.count(i) > 1 and i not in b:
        b.append(i)
print(' '.join(b))