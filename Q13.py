#13.Write a program that asks the user for their birth year and calculates their age.
from datetime import datetime
birth_year=int(input("Enter your birth year: "))
curr_year=datetime.now().year
age=curr_year - birth_year
print("Age: ",age)
