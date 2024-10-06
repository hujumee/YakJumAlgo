N = int(input())
board = [[0 for _ in range(N)] for _ in range(N)]
count = 0

def backtracking(order):
    global board, count
    if order == N:
        count += 1
        return
    
    for i in range(N):
        if board[order][i] == 0:
            place_q(order, i, 1)
            backtracking(order+1)
            place_q(order, i, 0)
        elif i == N-1:
            return 
    
def place_q(row, col, case):
    dr = [0, 0, 1, -1, -1, -1, 1, 1]
    dc = [1, -1, 0, 0, -1, 1, -1, 1]

    if case == 1:
        board[row][col] = 2
        for k in range(8):
            x = 1
            while -1 < row+x*dr[k] < N and -1 < col + x*dc[k] < N:
                nr, nc = row + x * dr[k], col + x*dc[k]
                board[nr][nc] += 1
                x += 1
    else:
        board[row][col] = 0
        for k in range(8):
            x = 1
            while -1 < row+x*dr[k] < N and -1 < col + x*dc[k] < N:
                nr, nc = row + x * dr[k], col + x*dc[k]
                board[nr][nc] -= 1
                x += 1


backtracking(0)
print(count)