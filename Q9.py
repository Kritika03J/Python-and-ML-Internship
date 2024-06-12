#9.Write a python program that checks if a substring is present in a given string.
str1 = input("Enter string: ")
str2 = input("Enter substring: ")
if str2 in str1:
    result=True
else:
    result=False
print("Substring in string: ",result)
