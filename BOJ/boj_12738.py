## 가장 긴 증가하는 부분수열 3
import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
answer = [-1000000001]

for item in arr:
    if answer[-1] < item:
        answer.append(item)
    else:
        left = 0
        right = len(answer)
        while left < right:
            mid = (left + right) // 2
            if answer[mid] < item:
                left = mid + 1
            else:
                right = mid
        answer[right] = item

print(len(answer)-1)
