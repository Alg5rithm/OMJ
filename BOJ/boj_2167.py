## 2차원 배열의 합
import sys

N, M = map(int, sys.stdin.readline().split())
# 초기화
array_list = [[0 for col in range(M)] for row in range(N)]
dp_list = [[0 for col in range(M + 1)] for row in range(N + 1)]
for i in range(N):
    value_list = list(map(int, sys.stdin.readline().split()))
    for j in range(M):
        array_list[i][j] = value_list[j]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        dp_list[i][j] = array_list[i - 1][j - 1] + dp_list[i - 1][j] + dp_list[i][j - 1] - dp_list[i - 1][j - 1]

K = int(sys.stdin.readline())
for _ in range(K):
    i, j, x, y = map(int, sys.stdin.readline().split())
    print(dp_list[x][y] - dp_list[x][j - 1] - dp_list[i - 1][y] + dp_list[i - 1][j - 1])
