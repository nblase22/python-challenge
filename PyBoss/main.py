#PyBoss

import os
import csv

#declare variables
name = []
dob = []
emp_id = []
ssn = []
state = []


#import the first CSV file of employee data
filename = input("Input the name of the data file: ")

empdata_csv = os.path.join('Resources', filename)

with open(empdata_csv, newline="") as csvfile:
    next(csvfile, None)
    csvreader = csv.reader(csvfile, delimiter = ",")
