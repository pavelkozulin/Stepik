a = int(input())
b = int(input())
c = int(input())

if a >= b and a >= c:
    max = a
    if b >= c:
        min = c
        rest = b
    else:
        min = b
        rest = c
if b >= a and b >= c:
    max = b
    if a >= c:
        min = c
        rest = a
    else:
        min = a
        rest = c
if c >= a and c >= b:
    max = c
    if a >= b:
        min = b
        rest = a
    else:
        min = a
        rest = b
print(max)
print(min)
print(rest)
