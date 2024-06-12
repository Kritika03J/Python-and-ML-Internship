#14.Write a program that reads multiple lines of input from the user until they enter on an empty line, then prints all the lines.
lines = []
print("Enter lines of text (press Enter on an empty line to finish):")
while True:
    line = input()
    if line == "":
        break
    lines.append(line)
user_lines = lines
print("You entered:")
for line in user_lines:
    print(line)
