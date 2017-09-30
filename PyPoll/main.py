#PyPoll

import os
import csv

#declare variables
totVote = 0
winIndex = 0
tie = 0
candidateList = []
votePer = []
percentPer = []
tieParties = []

#Import CSV file of bank data
filename = input("Input the name of the data file: ")

pypoll_csv = os.path.join('Resources', filename)

with open(pypoll_csv, newline="") as csvfile:
    next(csvfile, None)
    csvreader = csv.reader(csvfile, delimiter = ",")


    for row in csvreader:
        # get total number of votes cast
        totVote = totVote + 1

        #get list of candidates
        candidateList.append(row[2])

#Use set function to limit the list to just the unique names
candidateListSet = list(set(candidateList))

#Get the number of votes per candidate
for candidate in candidateListSet:
    votePer.append(candidateList.count(candidate))

#get the percentage of votes per candidate
for i in range(0, len(candidateListSet)):
    pPer = float(votePer[i]/totVote * 100)
    pPer = round(pPer, 2)
    percentPer.append(pPer)

#Find the index of the winner
for i in range(1, len(votePer)):
    if votePer[i] > votePer[i-1]:
        winIndex = i
    elif votePer[i] == votePer[i-1]:
        tieParties.append(candidateListSet[i])
        tieParties.append(candidateListSet[i-1])
        tie = 1

tieParties = list(set(tieParties))

#Export text File
output = os.path.join('Outputs', "output.txt")
outFile = open(output, "w")

outFile.write("Election Results" + '\n')
outFile.write("-----------------------------" + '\n')
outFile.write("Total Votes: " + str(totVote) + '\n')
outFile.write("-----------------------------" + '\n')
for i in range(0, len(candidateListSet)):
    outFile.write(candidateListSet[i] + ": " + str(percentPer[i]) + "% (" + str(votePer[i]) + ")" + '\n')
outFile.write("-----------------------------" + '\n')
outFile.write("Winner: " + candidateListSet[winIndex])
outFile.close()


#Print to screen
print()
print("Election Results")
print("-----------------------------")
print("Total Votes: " + str(totVote))
print("-----------------------------")
for i in range(0, len(candidateListSet)):
    print(candidateListSet[i] + ": " + str(percentPer[i]) + "% (" + str(votePer[i]) + ")")
print("-----------------------------")
if tie != 1:
    print("Winner: " + candidateListSet[winIndex])

else:
    print("It's a tie between: ")
    for party in tieParties:
        print(party)