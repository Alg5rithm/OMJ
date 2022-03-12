## 수 정렬하기 3

import sys

N = int(sys.stdin.readline())
numbers = [0] * 10000

for _ in range(N):
    num = int(sys.stdin.readline())
    numbers[num] += 1

for i in range(len(numbers)):
    if numbers[i] != 0:
        for j in range(numbers[i]):
            print(i)

# sort()의 방법으로는 메모리 초과 발생
