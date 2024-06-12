#25.Write a program that copies the contents of one text file to another.
source_file = "C:\\Users\\Kritika Jain\\Desktop\\1.txt"
destination_file = "C:\\Users\\Kritika Jain\\Desktop\\2.txt"
try:
    with open(source_file, 'r') as src:
        content = src.read()
    with open(destination_file, 'w') as dest:
        dest.write(content)
    print(f"Contents of {source_file} have been copied to {destination_file}.")
except FileNotFoundError:
    print(f"The file {source_file} does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
