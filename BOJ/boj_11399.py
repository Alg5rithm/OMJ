# ATM

import sys

n = int(sys.stdin.readline())
data_list = list(map(int, sys.stdin.readline().split(' ')))
data_list.sort()
total_value = 0
add_value = 0

for data in data_list:
    add_value += data
    total_value += add_value

print(total_value)
