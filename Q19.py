#19.Write a python program that removes all punctuation from a given string.
str = input("Enter a string: ")
punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
result = ""
for char in str:
    if char not in punctuation:
        result += char
print("Original: ",str)
print("Without punctuation: ",result)
