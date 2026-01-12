def is_safe(board, row, col):
    for i in range(col):
        # Check row and both diagonals
        if board[i] == row or \
           abs(board[i] - row) == abs(i - col):
            return False
    return True

def solve(board, col):
    if col == 8: return True # All queens placed
    
    for row in range(8):
        if is_safe(board, row, col):
            board[col] = row
            if solve(board, col + 1): return True
            board[col] = -1 # Backtrack
    return False

# Execution
board = [-1] * 8
if solve(board, 0):
    for r in range(8):
        line = ["Q" if board[c] == r else "." for c in range(8)]
        print(" ".join(line))
else:
    print("No solution")