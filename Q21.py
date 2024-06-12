#21.Write a python program that counts the occurrences of a specific element in a list.
list1 = [x for x in input("Enter a list of elements separated by spaces: ").split()]
element=input("Enter a specific element to be found in list: ")
frequency = 0
for x in list1:
    if x==element:
        frequency += 1
print(element, " : ", frequency)
