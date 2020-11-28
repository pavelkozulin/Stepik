a = 0
b = []
while a <= 100:
    a = int(input())
    if 100 >= a >= 10:
        b.append(a)
print(*b, sep='\n')
