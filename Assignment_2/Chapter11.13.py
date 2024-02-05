def locateLargest(a):
    if not a or not a[0]:
        return None  # Return None for invalid lists

    max_value = a[0][0]
    max_location = [0, 0]

    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] > max_value:
                max_value = a[i][j]
                max_location = [i, j]
    return max_location

n = int(input("Enter the number of rows the list: "))
matrix = []
for i in range(n):
    rows=[]
    data = input(f"Enter a row: ")
    elm = data.split()
    for j in range(0, len(elm)):
        row = float(elm[j])
        rows.append(row)
    matrix.append(rows)

print("\nEntered Matrix:")
for row in matrix:
    print(row)

location = locateLargest(matrix)
if location:
    print("\nLocation of the largest element:", location)
else:
    print("\nThe input matrix is invalid.")
