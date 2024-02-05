import random
def generate_matrix(rows, cols):
    matrix=[]
    for i in range(rows):
        r=[]
        for j in range(cols):
            elm=random.randint(0, 1)
            r.append(elm)
        matrix.append(r)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(row)

def find_most_ones(matrix):
    max_ones_row_index = max(range(len(matrix)), key=lambda i: matrix[i].count(1))
    max_ones_col_indices = [j for j in range(len(matrix[0])) if any(matrix[i][j] == 1 for i in range(len(matrix)))]
    return max_ones_row_index, max_ones_col_indices

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

matrix = generate_matrix(rows, cols)
print("\nGenerated Matrix:")
print_matrix(matrix)

max_ones_row_index, max_ones_col_indices = find_most_ones(matrix)

print("\nThe largest row index:", max_ones_row_index)
print("The largest column index:", ", ".join(map(str, max_ones_col_indices)))