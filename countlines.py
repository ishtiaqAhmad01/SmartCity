import os

def count_lines_of_code(directory, extension=".py"):
    total_lines = 0
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    lines = f.readlines()
                    total_lines += len(lines)
    return total_lines

# Replace 'your_project_directory' with the path to your project folder
project_directory = r"C:\Users\ISHTIAQ\OneDrive\Desktop\New folder"
lines_of_code = count_lines_of_code(project_directory)
print(f"Total lines of code: {lines_of_code}")
