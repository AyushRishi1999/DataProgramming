import keyword
def countKeywords(content):
    count = {kw: 0 for kw in keyword.kwlist}
    for line in content:
        for word in line.split():
            if word in count:
                count[word] += 1

    return count

name = input("Enter the Python source code filename: ")
try:
    with open(name, 'r') as file:
        content = file.readlines()
    result = countKeywords(content)
    print("Keyword Counts:")
    for kw, count in result.items():
        print(f"{kw}: {count}")

except FileNotFoundError:
    print(f"File '{name}' not found.")
except IOError:
    print(f"Error reading file '{name}'.")
except Exception as e:
    print(f"An error occurred: {e}")
