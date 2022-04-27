## 가장 긴 증가하는 부분수열 5
import sys

N = sys.stdin.readline()
arr = list(map(int, sys.stdin.readline().split()))
dp = [-1000000001]
index = []

for item in arr:
    if dp[-1] < item:
        dp.append(item)
        index.append(dp.index(item))
    else:
        left = 0
        right = len(dp)
        while left < right:
            mid = (left + right) // 2
            if dp[mid] < item:
                left = mid + 1
            else:
                right = mid
        dp[right] = item
        index.append(right)

count = 1
answer = []
for i in range(len(index)):
    if index[i] == count:
        answer.append(arr[i])
        count += 1

print(len(dp) - 1)
print(*answer)
