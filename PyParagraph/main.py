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

print(wordCount)


# figure out number of sentences
sentences = re.split(r' *[\.\?!][\'"\)\]]* *', paragraph)
print(len(sentences))