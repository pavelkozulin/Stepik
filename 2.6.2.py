n = int(input())
if n ==1:
    print('1')
else:
    b = []
    while True:
        for i in range(n):
            for j in range(i):
                b.append(i)
        i += 1
        if len(b) > n:
            break
    
    b = b[:n]
    str1 = ' '.join(str(e) for e in b)
    print(str1)
    