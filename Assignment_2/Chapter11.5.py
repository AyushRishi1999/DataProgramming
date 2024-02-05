def addMatrix(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        raise ValueError("Matrices must have the same dimensions for addition")

    result = [[0 for _ in range(len(a[0]))] for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            result[i][j] = a[i][j] + b[i][j]
    return result

matrix1 = []
data1 = input("Enter matrix 1: ")
elm1 = data1.split()
for i in range(0,len(elm1),3):
    rows = []
    for j in range(i,i+3):
        row = float(elm1[j])
        rows.append(row)
    matrix1.append(rows)
matrix2 = []
data2 = input("Enter matrix 2: ")
elm2 = data1.split()
for i in range(0,len(data1),3):
    rows = []
    for j in range(i, i+3):
        row = float(elm2[j])
        rows.append(row)
    matrix2.append(rows)

result_matrix = addMatrix(matrix1, matrix2)
print("Matrix 1:")
for row in matrix1:
    print(row)

print("\nMatrix 2:")
for row in matrix2:
    print(row)

print("\nResult Matrix:")
for row in result_matrix:
    print(row)
