# backtracking 기법 이용
# 시간초과

import sys


def DFS(N, current_row, current_candidate, final_result):
    if current_row == N:
        final_result.append(current_candidate[:])
        return
    for candidate_col in range(N):
        if is_available(current_candidate, candidate_col):
            current_candidate.append(candidate_col)
            DFS(N, current_row + 1, current_candidate, final_result)
            current_candidate.pop()  # backtracking


def is_available(candidate, current_col):
    current_row = len(candidate)
    for queen_row in range(current_row):
        if candidate[queen_row] == current_col or abs(candidate[queen_row] - current_col) == current_row - queen_row:
            return False
    return True


def solve_n_queens(N):
    final_result = []
    DFS(N, 0, [], final_result)
    return final_result

N = int(sys.stdin.readline())
answer = solve_n_queens(N)[0]
for i in range(N):
    print(answer[i])
