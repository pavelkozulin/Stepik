z = int(input())

a = z // 100000
z = z - a * 100000
b = z // 10000
z = z - b * 10000
c = z // 1000
z = z - c * 1000
d = z // 100
z = z - d * 100
e = z // 10
z = z - e * 10
f = z

if a + b + c == d + e + f:
    print('Счастливый')
else:
    print('Обычный')
