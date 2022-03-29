import sys

N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split()))
answer = []
answer_sum = 0

for i in range(1, len(N_list) + 1):
    if len(answer) == 0:
        answer.append(N_list[0])
        answer_sum += N_list[0]
    else:
        next_num = (i * N_list[i - 1]) - answer_sum
        answer.append(next_num)
        answer_sum += next_num

for item in answer:
    print(item, end=' ')
