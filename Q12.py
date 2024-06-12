#12.Write a python program that calculates the sum of the digits of a given number.
n = int(input("Enter a number: "))
sum = 0
while (n != 0):
    sum = sum + int(n % 10)
    n = int(n / 10)
print("Sum of digits: ", sum)
