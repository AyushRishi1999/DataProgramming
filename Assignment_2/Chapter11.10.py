import random
matrix = []
for r in range(4):
    row = []
    for c in range(4):
        row.append(random.randint(0,1))
    matrix.append(row)

maxRowIndex = 0
maxRowCount = 0
maxColIndex = 0
maxColCount = 0

for r in range(len(matrix)):
    rowCount = colCount = 0
    for c in range(len(matrix[0])):
        if matrix[r][c] == 1:
            rowCount += 1
        if matrix[c][r] == 1:
            colCount += 1
    if rowCount > maxRowCount:
        maxRowCount = rowCount
        maxRowIndex = r
    if colCount > maxColCount:
        maxColCount = colCount
        maxColIndex = r

print('The largest row index:', str(maxRowIndex))
print('The largest column index:', str(maxColIndex))