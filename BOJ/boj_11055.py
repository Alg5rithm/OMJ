## 가장 큰 증가 부분 수열
# 1 100 2 50 60 3 5 6 7 8
# 1 100 2 50 60 4 70 6 7 8

import sys

N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
DP_list = num_list.copy()

for i in range(1, N):
    for j in range(i):
        if num_list[i] > num_list[j]:
            DP_list[i] = max(DP_list[j] + num_list[i], DP_list[i])

print(max(DP_list))
