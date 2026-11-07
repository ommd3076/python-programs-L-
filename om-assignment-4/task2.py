name = input("Enter your name: ")
clg = input("Enter clg: ")
crs = input("Enter course: ")
with open("output.txt", "w") as file:
    file.write(name )
with open("output.txt", "a") as file:
    file.write(clg )
with open("output.txt", "a") as file:
    file.write(crs )
with open("output.txt", "r") as file:
    for line in file:
        print(line, "\n")
