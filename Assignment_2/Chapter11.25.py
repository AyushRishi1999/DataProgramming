def isMarkovMatrix(m):
    # Check if each element is positive
    for row in m:
        if any(element <= 0 for element in row):
            return False

    # Check if the sum of elements in each column is 1
    num_columns = len(m[0])
    for j in range(num_columns):
        column_sum = sum(row[j] for row in m)
        if not column_sum == 1:
            return False

    return True

n = int(input("Enter the number of rows: "))
matrix = []
print(f"Enter a {n}-by-{n} matrix row by row:")
for i in range(n):
    rows=[]
    data = input()
    elm = data.split()
    for j in range(0, len(elm)):
        row = float(elm[j])
        rows.append(row)
    matrix.append(rows)

if isMarkovMatrix(matrix):
    print("\nIt is a Markov matrix.")
else:
    print("\nIt is not a Markov matrix.")
