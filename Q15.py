#15.Write a program that reads data from a CSV file and prints it to the console.
import csv
file_path = "C:\\Users\\Kritika Jain\\Salary.csv"
with open(file_path, mode='r', newline='') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(', '.join(row))
