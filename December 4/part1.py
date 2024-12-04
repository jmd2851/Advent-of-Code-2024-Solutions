import re
board = []
xmas = "XMAS"
samx = "SAMX"
count = 0
with open("input.txt") as f:
    for line in f:
        board.append(line.strip())

def get_all(string: str):
    results = re.findall(xmas, string)
    rev_results = re.findall(samx, string)
    return len(results) + len(rev_results)

# horiz
for row in board:
    count += get_all(row)

# vert
for i in range(len(board)):
    col = [col[i] for col in board]
    colstr = ""
    for colchar in col:
        colstr += colchar
    count += get_all(colstr)

l_to_r_diag_top = []
for start_row_index in range(len(board)):
    diag_str = ""
    col_index = 0
    for continue_row_index in range(start_row_index, -1, -1):
        diag_str += board[continue_row_index][col_index]
        col_index += 1
    l_to_r_diag_top.append(diag_str)

for diag in l_to_r_diag_top:
    if len(diag) >= 4:
        count += get_all(diag)

r_to_l_diag_top = []
for start_row_index in range(len(board)):
    diag_str = ""
    col_index = len(board) - 1
    for continue_row_index in range(start_row_index, -1, -1):
        diag_str += board[continue_row_index][col_index]
        col_index -= 1
    r_to_l_diag_top.append(diag_str)

for diag in r_to_l_diag_top:
    if len(diag) >= 4:
        count += get_all(diag)

l_to_r_diag_bottom = []
for start_row_index in range(len(board) - 1, 0, -1):
    diag_str = ""
    col_index = len(board) - 1
    for continue_row_index in range(start_row_index, len(board)):
        diag_str += board[continue_row_index][col_index]
        col_index -= 1
    l_to_r_diag_bottom.append(diag_str)

for diag in l_to_r_diag_bottom:
    if len(diag) >= 4:
        count += get_all(diag)

r_to_l_diag_bottom = []
for start_row_index in range(len(board) - 1, 0, -1):
    diag_str = ""
    col_index = 0
    for continue_row_index in range(start_row_index, len(board)):
        diag_str += board[continue_row_index][col_index]
        col_index += 1
    r_to_l_diag_bottom.append(diag_str)

for diag in r_to_l_diag_bottom:
    if len(diag) >= 4:
        count += get_all(diag)

print(count)
    