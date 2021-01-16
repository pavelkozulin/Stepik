a = int(input())
s = a
b = a * a
while s != 0:
    a = int(input())
    s += a
    b += a * a
#    print('s', s)
#    print('b', b)
print(b)