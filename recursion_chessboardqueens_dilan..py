board = [input() for _ in range(8)]

columns = set()
diag1 = set()
diag2 = set()

count = 0

def solve(row):
    global count
    if row == 8:
        count += 1
        return
    for col in range(8):
        if board[row][col] == '.':
            if col not in columns and (row + col) not in diag1 and (row - col) not in diag2:
                columns.add(col)
                diag1.add(row + col)
                diag2.add(row - col)
                solve(row + 1)
                columns.remove(col)
                diag1.remove(row + col)
                diag2.remove(row - col)

solve(0)
print(count)
