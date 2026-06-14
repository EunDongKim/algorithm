def solution(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1 :
                for x in range(-1,2):
                    for y in range(-1,2):
                        try :
                            if board[i+x][j+y] != 1 and i+x != -1 and j+y != -1:
                                board[i+x][j+y] = -1
                        except : continue
    count = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                count += 1
    return count
