## 정수 삼각형

import sys

N = int(sys.stdin.readline())
input_list = [[0 for _ in range(N)] for _ in range(N)]
DP = [[0 for _ in range(N)] for _ in range(N)]

for i in range(0, N):
    tmp = list(map(int, sys.stdin.readline().split()))
    for j in range(0, i+1):
        input_list[i][j] = tmp[j]

for i in range(0, N):
    for j in range(0, N):
        DP[i][j] = max(DP[i-1][j-1], DP[i-1][j]) + input_list[i][j]

print(max(DP[-1]))
