n = int(input())
a = []
while len(a) < n:
    for i in range(1, n):
        for j in range (i):
           a.append(i)
a = a[:n]
print(' '.join((str(e) for e in a)))