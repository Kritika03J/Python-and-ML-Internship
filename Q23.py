#23.Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input.
temp=float(input("Enter temperature: "))
scale=input("Enter c/C for Celsius or f/F for Fahrenheit: ")
if (scale=='c' or scale=='C'):
    f=((9*temp)/5)+32
    print("Temperature in Fahrenheit is: ",f,"F")
elif (scale=='f' or scale=='F'):
    c=(temp-32)*(5/9)
    print("Temperature in Celsius is: ", c, "C")
