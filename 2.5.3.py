a = sorted([x for x in input().split(' ')]) + ['o']
print(' '.join([a[i]
for i in range(1, len(a) - 1)
if a[i] != a[i + 1] and a[i] == a[i - 1]]))
