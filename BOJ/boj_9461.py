import sys

n = int(sys.stdin.readline())
padovan = [0 for _ in range(101)]
padovan[1] = 1
padovan[2] = 1
padovan[3] = 1
padovan[4] = 2
padovan[5] = 2
for i in range(6, 101):
    padovan[i] = padovan[i - 5] + padovan[i - 1]

for i in range(n):
    T = int(sys.stdin.readline())
    print(padovan[T])
