import sys

N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))

N_list.sort()


def binary_search(search, start, end):
    if start > end:
        return 0
    medium = (start + end) // 2
    if N_list[medium] > search:
        return binary_search(search, start, medium - 1)
    elif N_list[medium] < search:
        return binary_search(search, medium + 1, end)
    else:
        return 1


for item in M_list:
    print(binary_search(item, 0, N - 1))
