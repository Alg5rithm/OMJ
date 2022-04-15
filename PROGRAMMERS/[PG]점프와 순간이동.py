## N
# 순간이동 : *2
# 점프 : +1

def solution(n):
    ans = 0
    while True:
        if n == 0:
            break
        if n % 2 != 0:
            n -= 1
            ans += 1
        else:
            n /= 2

    return ans