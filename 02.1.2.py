a = int(input())
b = int(input())

z = a
while z % b != 0:
    z += a
print(z)
