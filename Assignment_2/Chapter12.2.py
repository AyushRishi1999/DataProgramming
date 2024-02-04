class Location:
    def __init__(self, row=0, column=0, maxValue=0.0):
        self.row = row
        self.column = column
        self.maxValue = maxValue
def locateLargest(a):
    if not a or not a[0]:
        return None

    maxValue = a[0][0]
    maxLocation = Location()

    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] > maxValue:
                maxValue = a[i][j]
                maxLocation.row = i
                maxLocation.column = j
                maxLocation.maxValue = maxValue

    return maxLocation

def main():
    rows, columns = int(input("Enter the number of rows and columns in the list: "))

    for i in range(rows):
        m = float(input(f"Enter element at row {i}: "))
    result = locateLargest(m)

    print("\nThe location of the largest element is:")
    print(f"Row: {result.row}")
    print(f"Column: {result.column}")
    print(f"Max Value: {result.maxValue}")


if __name__ == "__main__":
    main()
