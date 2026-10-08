import os

print("Working directory:", os.getcwd())
print("File exists here:", os.path.exists("sample.txt"))

# with open("sample.txt", "r") as file:
#     for line in file:
#         print(line)
