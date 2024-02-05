def sumMajorDiagonal(m):
    if not m or not m[0] or len(m) != len(m[0]):
        return 0
    diagonal_sum = 0
    for i in range(len(m)):
        diagonal_sum += m[i][i]
    return diagonal_sum
def main():
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
    diagonal_sum = sumMajorDiagonal(matrix)
    print(f"\nSum of the elements in the major diagonal is {diagonal_sum}.")


if __name__ == "__main__":
    main()
