#PyBoss

import os
import csv

#declare variables
nameParse = []
dob = []
emp_id = []
ssn = []
state = []



#import the first CSV file of employee data
fileOne = "employee_data1.csv"
fileTwo = "employee_data2.csv"

empdataOne_csv = os.path.join('Resources', fileOne)
empdataTwo_csv = os.path.join('Resources', fileTwo)

with open(empdataOne_csv, newline="") as csvfile:
    next(csvfile, None)
    csvreader = csv.reader(csvfile, delimiter = ",")

    for row in csvreader:
        emp_id.append(row[0])
        nameParse.append(row[1])
        dob.append(row[2])
        ssn.append(row[3])
        state.append(row[4])


with open(empdataTwo_csv, newline="") as csvfiletwo:
    next(csvfiletwo, None)
    csvreadertwo = csv.reader(csvfiletwo, delimiter = ",")

    for row in csvreadertwo:
        emp_id.append(row[0])
        nameParse.append(row[1])
        dob.append(row[2])
        ssn.append(row[3])
        state.append(row[4])


name = [words for segments in nameParse for words in segments.split()]

first_name = name[::2]
last_name = name[1::2]


