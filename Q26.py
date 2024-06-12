#26.Write a program in python that checks if a string starts with a given prefix or ends with a given suffix.
string = input("Enter a string: ")
prefix = input("Enter prefix to check: ")
suffix = input("Enter suffix to check: ")
starts_with_prefix = string.lower().startswith(prefix.lower())
ends_with_suffix = string.lower().endswith(suffix.lower())
print(f"Starts with prefix '{prefix}': {starts_with_prefix}")
print(f"Ends with suffix '{suffix}': {ends_with_suffix}")
