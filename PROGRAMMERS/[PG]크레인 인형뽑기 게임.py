def solution(board, moves):
    basket = [] # 저장할 바구니
    answer = 0
    for item in moves: # 크레인이 인형을 집을 위치
        num = -1
        for i in range(len(board)):
            if board[i][item-1] != 0:
                num = board[i][item-1]
                board[i][item-1] = 0
                break
        if num != -1:
            if len(basket) != 0 and basket[-1] == num:
                basket.pop(-1)
                answer += 2
            else:
                basket.append(num)
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))