#22.Write a python program that returns the minimum and maximum values in a list of numbers.
numbers = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
max=min=numbers[0]
for x in numbers:
    if x>max:
        max=x
    if x<min:
        min=x
print("Maximum value: ",max)
print("Minimum value: ",min)
