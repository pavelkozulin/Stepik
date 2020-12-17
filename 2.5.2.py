a = [int(i) for i in input().split(' ')]
if len(a) != 1:
    print(*[a[j-1]+a[j+1-len(a)] for j in range(len(a))])
else:
    print(*a)
