
student_data = []
input_data = input("Enter students' names and their scores (e.g., John 85 Alice 92 Bob 78): ")
words = input_data.split()
for i in range(0, len(words), 2):
    name = words[i]
    score = int(words[i+1])
    student_data.append([score, name])

student_data.sort()
print("\nStudent names in increasing order of scores:")
for data in student_data:
    print(data[1],"\t",data[0])