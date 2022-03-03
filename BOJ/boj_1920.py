import sys

N = int(sys.stdin.readline())
data_list = list(map(int, sys.stdin.readline().split()))
data_list.sort()
M = int(sys.stdin.readline())
search_list = list(map(int, sys.stdin.readline().split()))


def binary_search(search, start, end):
    if start > end:
        return 0
    medium = (start + end) // 2
    if data_list[medium] > search:
        return binary_search(search, start, medium - 1)
    elif data_list[medium] < search:
        return binary_search(search, medium + 1, end)
    else:
        return 1


for item in search_list:
    print(binary_search(item, 0, N-1))
