a = [x for x in input().split()]
b = [a[i]
    for i in range(1, len(a)) 
    if a[i] in a[:i]]
print(' '.join(set(b)))

  
