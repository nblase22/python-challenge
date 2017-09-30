#PyBank

import os
import csv


#declare variables
totMonths = 0
revcount = 0
revchange =[]
revdata = []
datedata = []

#Import 1st CSV file of bank data
filename = input("Input the name of the data file: ")

pybank_csv = os.path.join('Resources', filename)

with open(pybank_csv, newline="") as csvfile:
    next(csvfile)
    csvreader = csv.reader(csvfile, delimiter = ",")

    #Determine total number of months in the dataset
    for row in csvreader:
        totMonths = totMonths + 1

        #Determine the total amount of revenue gained over the entire period
        revcount = revcount + int(row[1])

        #place the rev data and date data in separate lists for use later
        datedata.append(row[0])
        revdata.append(row[1])


#Average Change in Revenue between months over the entire period
for i in range(1, len(revdata)):
    revchange.append(int(revdata[i]) - int(revdata[i-1]))

avgchange = sum(revchange)/float(len(revchange))
avgchange = round(avgchange, 2)

#Greatest increase in revenue (date and amount) over the period
#Greatest decrease in revenue (date and amount) over the period
greatinc = max(revchange)
greatdec = min(revchange)
for i in range(0,len(revchange)):
    if revchange[i] == greatinc:
        gIncIndex = i
    elif revchange[i] == greatdec:
        gDecIndex = i

greatincmonth = datedata[gIncIndex + 1]
greatdecmonth = datedata[gDecIndex + 1]

#export text file with results to Outputs folder
output = os.path.join('Outputs', "output.txt")
outFile = open(output, "w")
outFile.write("Financial Analysis" + '\n')
outFile.write("-----------------------------" + '\n')
outFile.write("Total Months: " + str(totMonths) + '\n')
outFile.write("Total Revenue: $" + str(revcount)+ '\n')
outFile.write("Average Revenue Change: $" + str(avgchange)+ '\n')
outFile.write("Greatest Increase in Revenue: " + greatincmonth + " ($" + str(greatinc) + ")"+ '\n')
outFile.write("Greatest Decrease in Revenue: " + greatdecmonth + " ($" + str(greatdec) + ")"+ '\n')
outFile.close()


#print the analysis to the terminal
print()
print("Financial Analysis")
print("-----------------------------")
print("Total Months: " + str(totMonths))
print("Total Revenue: $" + str(revcount))
print("Average Revenue Change: $" + str(avgchange))
print("Greatest Increase in Revenue: " + greatincmonth + " ($" + str(greatinc) + ")")
print("Greatest Decrease in Revenue: " + greatdecmonth + " ($" + str(greatdec) + ")")