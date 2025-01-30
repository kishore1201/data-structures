def safe(board, row, col, N):
    # Check the left side of the row
    i = col
    while i >= 0:
        if board[row][i] == 1:
            return False
        i -= 1

    # Check upper diagonal on the left
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal on the left
    i, j = row, col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True

def Solve_N_Queen(board, col, N):
    if col >= N:
        return True

    for row in range(N):
        if safe(board, row, col, N):
            board[row][col] = 1  
            if Solve_N_Queen(board, col + 1, N):
                return True
            board[row][col] = 0  

    return False

N = 4  
board = [[0 for i in range(N)] for j in range(N)]

sol = Solve_N_Queen(board, 0, N)
if sol:
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()
else:
    print("No solution exists")
