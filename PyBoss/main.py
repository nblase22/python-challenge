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

#Convert state to appreviation
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

for m in range(0, len(state)):
    state[m] = us_state_abbrev[state[m]]


# Write the data to an output file
output_csv = os.path.join('Output', 'Employee_Data_Output.csv')
outputFile = open(output_csv, 'w', newline = '')
outputWriter = csv.writer(outputFile)

outputWriter.writerow(['Emp Id', 'First Name', 'Last Name', 'DOB', 'SSN', 'State'])

for n in range(0, len(first_name)):
    outputWriter.writerow([emp_id[n], first_name[n], last_name[n], dob[n], ssn[n], state[n]])

outputFile.close()




