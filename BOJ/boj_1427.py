# 소트인사이드

import sys

n = int(sys.stdin.readline())
numbers = list(map(int, str(n)))

numbers.sort(reverse=True)

print(''.join(str(n) for n in numbers))
