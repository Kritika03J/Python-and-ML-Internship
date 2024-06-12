#11.Write a python program that generates the first n numbers in the Fibonacci sequence.
n=int(input("Enter a number: "))
x0=0
x1=1
print("Fibonacci Sequence:")
for i in range(0,n):
    print(x0,end=" ")
    x2=x0+x1
    x0=x1
    x1=x2
