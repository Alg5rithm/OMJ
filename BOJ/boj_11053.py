## 가장 긴 증가하는 부분 수열
# 10 20 10 30 20 50
# 1 2 1 3 2 4

import sys

N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
DP_list = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if num_list[i] > num_list[j]:
            DP_list[i] = max(DP_list[j] + 1, DP_list[i])

print(max(DP_list))
