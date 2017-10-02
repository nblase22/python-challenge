#PyBoss

import os
import csv
import datetime

#declare variables
nameParse = []
dob = []
emp_id = []
ssn = []
state = []




#import the csv files of employee data
fileOne = "employee_data1.csv"
fileTwo = "employee_data2.csv"

empdataOne_csv = os.path.join('Resources', fileOne)
empdataTwo_csv = os.path.join('Resources', fileTwo)

#put the first file into a series of lists for manipulation
with open(empdataOne_csv, newline="") as csvfile:
    next(csvfile, None)
    csvreader = csv.reader(csvfile, delimiter = ",")

    for row in csvreader:
        emp_id.append(row[0])
        nameParse.append(row[1])
        dob.append(row[2])
        ssn.append(row[3])
        state.append(row[4])

# put the second file into a series of lists for manipulation
with open(empdataTwo_csv, newline="") as csvfiletwo:
    next(csvfiletwo, None)
    csvreadertwo = csv.reader(csvfiletwo, delimiter = ",")

    for row in csvreadertwo:
        emp_id.append(row[0])
        nameParse.append(row[1])
        dob.append(row[2])
        ssn.append(row[3])
        state.append(row[4])

#parse the names into a big list
name = [words for segments in nameParse for words in segments.split()]

#grab every other  element for first name from name list starting at first item
first_name = name[::2]

#grab every other element for last name from name list starting at second item
last_name = name[1::2]

#convert dob from yyyy-mm-dd to dd/mm/yyyy
for i in range(0, len(dob)):
    dob[i] = datetime.datetime.strptime(dob[i], '%Y-%m-%d').strftime('%m/%d/%y')

# * out the first five numerals in the ssn
for j in range(0, len(ssn)):
    ssnList = list(ssn[j])
    for k in range(0,3):
        ssnList[k] = '*'
    for l in range(4,6):
        ssnList[l] = '*'

    ssn[j] = "".join(ssnList)





