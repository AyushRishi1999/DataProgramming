import keyword
def count_keywords(file_content):
    keyword_count = {kw: 0 for kw in keyword.kwlist}

    for line in file_content:
        for word in line.split():
            if word in keyword_count:
                keyword_count[word] += 1

    return keyword_count

file_name = input("Enter the Python source code filename: ")
try:
    with open(file_name, 'r') as file:
        content = file.readlines()
    result = count_keywords(content)
    print("Keyword Counts:")
    for kw, count in result.items():
        print(f"{kw}: {count}")

except FileNotFoundError:
    print(f"File '{file_name}' not found.")
except IOError:
    print(f"Error reading file '{file_name}'.")
except Exception as e:
    print(f"An error occurred: {e}")
