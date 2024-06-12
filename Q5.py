#5.Write a program that takes a string input from the user and writes it to a text file.
filename = "C:\\Users\\Kritika Jain\\Desktop\\1.txt"
user_input = input("Enter a string to write to the file: ")
with open(filename, 'w') as file:
    file.write(user_input)
print("String written to ", filename)
