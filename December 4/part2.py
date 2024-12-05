board = []
count = 0
with open("input.txt") as f:
    for line in f:
        board.append(line.strip())

for row_index in range(1, len(board) - 1):
    for col_index in range(1, len(board) - 1):
        if board[row_index][col_index] == 'A':
            if board[row_index - 1][col_index - 1] == 'M': # top left M
                if board[row_index + 1][col_index + 1] == 'S': # bottom right S
                    if board[row_index + 1][col_index - 1] == 'M': # bottom left M
                        if board[row_index - 1][col_index + 1] == 'S': # top right S
                            count += 1
                    elif board[row_index + 1][col_index - 1] == 'S': # bottom left S
                        if board[row_index - 1][col_index + 1] == 'M': # top right M
                            count += 1

            if board[row_index - 1][col_index - 1] == 'S': # top left S
                if board[row_index + 1][col_index + 1] == 'M': # bottom right M
                    if board[row_index + 1][col_index - 1] == 'M': # bottom left M
                        if board[row_index - 1][col_index + 1] == 'S': # top right S
                            count += 1
                    elif board[row_index + 1][col_index - 1] == 'S': # bottom left S
                        if board[row_index - 1][col_index + 1] == 'M': # top right M
                            count += 1
            
print(count)