def multiplyMatrix(a, b):
    if len(a[0]) != len(b):
        print("Matrices cannot be multiplied. Number of columns in A must be equal to the number of rows in B.")
        return None
    result = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
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

resultMatrix = multiplyMatrix(matrix1, matrix2)
if resultMatrix:
    print("\nMatrix A:")
    for row in matrix1:
        print(row)
    print("\nMatrix B:")
    for row in matrix2:
        print(row)
    print("\nResult of Matrix Multiplication (A * B):")
    for row in resultMatrix:
        print(row)
