#wap to solve 4 queen promblem
def is_safe(board, row, col):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i] == col:
            return False

        # Check diagonals
        if abs(board[i] - col) == abs(i - row):
            return False

    return True

def solve_queens(board, row):
    n = len(board)
    if row >= n:
        return True

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            if solve_queens(board, row + 1):
                return True
            board[row] = -1

    return False

def solve_n_queens(n):
    board = [-1] * n
    if not solve_queens(board, 0):
        print("No solution exists")
        return None

    return board

def print_board(board):
    n = len(board)
    for row in range(n):
        for col in range(n):
            if board[row] == col:
                print("Q", end=" ")
            else:
                print(".", end="")
        print()

n = 4
solution = solve_n_queens(n)
if solution:
    print("Queens positions in each row:", solution)
    print_board(solution)
