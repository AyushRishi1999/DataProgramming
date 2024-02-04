def prefix(s1, s2):
    common_prefix = ""
    min_length = min(len(s1), len(s2))

    for i in range(min_length):
        if s1[i] == s2[i]:
            common_prefix += s1[i]
        else:
            break

    return common_prefix

s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")
common = prefix(s1, s2)
if common:
    print(f"The common prefix of '{s1}' and '{s2}' is: {common}")
else:
    print("The two strings have no common prefix.")

