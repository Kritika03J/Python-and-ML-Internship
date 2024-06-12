#24.Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input and print the result.
x=float(input("Enter 1st number: "))
y=float(input("Enter 2nd number: "))
op=input("Enter operator(+, -, *, /): ")
if (op=='+'):
    res=x+y
elif (op=='-'):
    res=x-y
elif (op=='*'):
    res=x*y
elif (op=='/'):
    if y==0:
        res='Division by zero not possible.'
    else:
        res=x/y
print(x, op, y, " = ", res)
