def sumMajorDiagonal(m):
    if not m or not m[0] or len(m) != len(m[0]):
        return 0
    diagonalSum = 0
    for i in range(len(m)):
        diagonalSum += m[i][i]
    return diagonalSum

n = int(input("Enter the size of the square matrix (n): "))
matrix = []
for i in range(n):
    rows=[]
    data = input(f"Enter a {n}-by-{n} matrix row for row {i+1}: ")
    elm = data.split()
    for j in range(0, len(elm)):
        row = float(elm[j])
        rows.append(row)
    matrix.append(rows)
print(f"\nThe {n} * {n} matrix is:")
for row in matrix:
    print(row)
diagonalSum = sumMajorDiagonal(matrix)
print(f"\nSum of the elements in the major diagonal is {diagonalSum}.")
