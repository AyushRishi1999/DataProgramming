import os
def count_files(directory):
    try:
        files = os.listdir(directory)
        file_count = len(files)
        print(f"Number of files in '{directory}': {file_count}")

        for file in files:
            file_path = os.path.join(directory, file)
            if os.path.isdir(file_path):
                count_files(file_path)

    except FileNotFoundError:
        print(f"Directory '{directory}' not found.")
    except PermissionError:
        print(f"Permission error accessing directory '{directory}'.")

user_directory = input("Enter a directory path: ")
count_files(user_directory)
