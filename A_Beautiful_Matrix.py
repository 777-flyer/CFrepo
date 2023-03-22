matrix = []

for i in range(5):
    row = input().split()
    for j in range(5):
        row[j] = int(row[j])
    matrix.append(row)
    
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            one_row, one_col = i, j
            break

moves = (one_row - 2) if one_row > 2 else (2 - one_row)
moves += (one_col - 2) if one_col > 2 else (2 - one_col)

print(moves)
