#6.Write a program that reads the content of a text file and prints it to the console.
filename = "C:\\Users\\Kritika Jain\\Desktop\\1.txt"
try:
    with open(filename, 'r') as file:
        content = file.read()
    print("File content:")
    print(content)
except FileNotFoundError:
    print(f"The file {filename} does not exist.")
