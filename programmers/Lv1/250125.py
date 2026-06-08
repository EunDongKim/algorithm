def solution(board, h, w):
    answer = 0
    target = board[h][w]

    if h != 0 and board[h-1][w] == target : answer += 1
    if w != 0 and board[h][w-1] == target : answer += 1
    if h != len(board)-1 and board[h+1][w] == target : answer += 1
    if w != len(board[0])-1 and board[h][w+1] == target : answer += 1
    
    return answer