import sys

a, b, c = map(int, sys.stdin.readline().split(' '))

if a > b:
    if a > c:
        print(a * 100)
    elif a < c:
        print(c * 100)
    else:
        print(1000 + a * 100)
elif a < b:
    if b > c:
        print(b * 100)
    elif b < c:
        print(c * 100)
    else:
        print(1000 + b * 100)
elif a == b:
    if b > c or b < c:
        print(1000 + a * 100)
    else:
        print(10000 + a * 1000)
