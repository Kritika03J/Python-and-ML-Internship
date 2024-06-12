#20.Write a python program that takes a list of numbers and returns their sum.
numbers = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
result = sum(numbers)
print("The sum of the numbers is: ", result)
