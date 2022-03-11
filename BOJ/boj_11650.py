# 좌표 정렬하기
import sys

n = int(sys.stdin.readline().strip())

points = [[0 for i in range(2)] for i in range(n)]
# x_list = [0 for i in range(n)]
# y_list = [0 for i in range(n)]

for i in range(n):
    input_point = list(map(int, sys.stdin.readline().split()))
    points[i][0] = input_point[0]
    points[i][1] = input_point[1]

points.sort()

for i in range(n):
    print(points[i][0], points[i][1])
