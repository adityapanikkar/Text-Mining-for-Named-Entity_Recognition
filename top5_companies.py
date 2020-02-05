#Code to generate top5 companies
import spacy
from collections import Counter
import os
import en_core_web_sm

# nlp is the object used for POS tagging using spaCy
nlp = en_core_web_sm.load()

def load_file_names(fpath):
    '''Loads file names in the path'''
    return [filename for filename in os.listdir(fpath)]

#Gives the parent directory path
mypath='D:/Aditya/AUT/Text mining/Assignment 2 data/CCAT/'

#Creates a list of all the files in the parent directory
filelist=load_file_names(mypath)
print(filelist)

# Creating an empty List
plist =[]

# Creating a compare list to eliminate non-needed organizations. This was done after the first iteration gave these names
comparelist= ['Reuters','EPS','PCT','ACTUAL']

# A loop which incrementally loops through each file path created by concatenating the homepath and filenames
for z in range(len(filelist)):
    mytext = open(mypath + filelist[z], "r") #This reads each file
    mytext = mytext.read()
    # POS tagging each file using the object NLP of spaCy
    doc=nlp(mytext)

    #This checks for the POS tags with the label "ORG" and writes then into a list
    for X in doc.ents:
        if(X.label_=='ORG'):
            plist.append(X.text)
# print(plist)

#Finding out the top 10 frequent Organizations as we need to eliminate a few that are incorrectly identified
plist1 = (Counter(plist).most_common(10))

#REmoving Reuters, EPS, PCT, Actual from the list
plist1.remove(plist1[0])
plist1.remove(plist1[0])
plist1.remove(plist1[2])
plist1.remove(plist1[2])
plist1.remove(plist1[4])

#Execute this to see the frequency of the top mentioned Organization
# print(plist[0])


#Since the resulting list gives the string and number of times it has appeared, we extract just the string by using this command
# Execute this to check the required output
# print(plist1[0][0])

#Writing just the names of the Top5 entities in a file
for a in range(len(plist1)):
    file2 = open("D:/Aditya/AUT/Text mining/Assignment 2 data/top5.txt","a+")
    file2.write(str(plist1[a]))