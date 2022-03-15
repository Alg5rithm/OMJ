## Z

def recur_visit(n, x, y):
    global result
    #  종료조건
    if n == 2:
        if x == X and y == Y:
            print(result)
            return
        result += 1
        if x == X and y + 1 == Y:
            print(result)
            return
        result += 1
        if x + 1 == X and y == Y:
            print(result)
            return
        result += 1
        if x + 1 == X and y + 1 == Y:
            print(result)
            return
        result += 1
        return
    recur_visit(n / 2, x, y)
    recur_visit(n / 2, x, y + n / 2)
    recur_visit(n / 2, x + n / 2, y)
    recur_visit(n / 2, x + n / 2, y + n / 2)


import sys

N, X, Y = map(int, sys.stdin.readline().split(' '))
result = 0

recur_visit(2 ** N, 0, 0)
