#18.Write a python program that checks if two strings are anagrams of each other.
str1 = input("Enter 1st string: ")
str2 = input("Enter 2nd string: ")
s1 = str1.replace(" ","").lower()
s2 = str2.replace(" ", "").lower()
result = sorted(s1)==sorted(s2)
if result==True:
    print("Strings are Anagrams of each other.")
else:
    print("Strings are NOT Anagrams of each other.")
