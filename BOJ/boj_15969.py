import sys

N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
num_list.sort()

print(num_list[N - 1] - num_list[0])
