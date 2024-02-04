# Function to check if a list is sorted in increasing order
def isSorted(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))

# Test program
user_input = input("Enter a list of numbers separated by spaces: ")

# Convert the input string to a list of floats
number_list = [float(num) for num in user_input.split()]

# Check if the list is sorted and display the result
if isSorted(number_list):
    print("The entered list is sorted in increasing order.")
else:
    print("The entered list is not sorted in increasing order.")
