import sys

n = int(sys.stdin.readline())

numbers = [0 for _ in range(1001)]
numbers[1] = 1
numbers[2] = 2
for i in range(3, n + 1):
    numbers[i] = numbers[i - 1] + numbers[i - 2]

print(numbers[n] % 10007)
