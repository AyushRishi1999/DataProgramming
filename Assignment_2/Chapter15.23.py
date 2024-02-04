def display_permutation(s):
    display_permutation_helper("", s)
def display_permutation_helper(s1, s2):
    if not s2:
        print(s1)
    else:
        for i in range(len(s2)):
            new_s1 = s1 + s2[i]
            new_s2 = s2[:i] + s2[i+1:]
            display_permutation_helper(new_s1, new_s2)

st = input("Enter a string: ")
display_permutation(st)
