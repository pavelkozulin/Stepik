a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a < 11:
    if b < 11:
        if c < 11:
                if d < 11:
                    print('', end = '\t')
                    for z in range(d - c + 1):
                        print((c + z), end = '\t')
                    print()
                    for i in range(b - a + 1):
                        print(a + i, end = ('\t'))
                        for j in range(d - c + 1):
                            print((c + j) * (a + i), end = '\t')
                        print()
