import os
import re

# set up the txt file for import
filename = input("Input the name of the file containing the paragraph to be read: ")

paragraph_file = os.path.join('resources', filename)

# pull the paragraph into python
with open(paragraph_file, 'r') as txtFile:
    paragraph = txtFile.read().replace("\n", " ")





# determine the word count
wordList = paragraph.split()
wordCount = len(wordList)



# figure out number of sentences
sentences = re.split(r' *[\.\?!][\'"\)\]]* *', paragraph)

# get average letter count
word_breakout = []
for item in sentences:
    word_breakout.append(item.split())

flat_breakout = []
for sublist in word_breakout:
    for item in sublist:
        flat_breakout.append(item)

letterCount = 0
for word in flat_breakout:
    letterCount = letterCount + len(word)

avg_letter = letterCount / wordCount



# get average sentence length