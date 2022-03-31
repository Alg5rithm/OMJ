import sys

N = int(sys.stdin.readline())
answer_list = list(map(str, sys.stdin.readline().strip()))
count = 1
answer = 0
bonus = 0

for i in range(len(answer_list)):
    if answer_list[i] == 'O':
        answer += count
        bonus += 1
        if answer_list[i-1] == 'O' and i > 0:
            answer += bonus
        else:
            bonus = 0
    count += 1

print(answer)

# 8
# XOOOXOOX

