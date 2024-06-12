#3.Write a python program that calculates the factorial of a given number.
x = int(input("Enter a number: "))
fact = 1
if x>1:
    for i in range(2,x+1):
        fact*=i
else:
    pass
print("Factorial: ",fact)