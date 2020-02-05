import spacy
from spacy import displacy
from collections import Counter
import os
import en_core_web_sm
nlp = en_core_web_sm.load()


def load_file_names(fpath):
    '''Loads  file data for a specified subset'''
    return [filename for filename in os.listdir(fpath)]

#Gives the parent directory path
mypath='D:/Aditya/AUT/Text mining/Assignment 2 data/CCAT/'

#Creates a list of all the files in the parent directory
filelist=load_file_names(mypath)
plist =[]
comparelist= ['Reuters','EPS','PCT','ACTUAL']
companies=['ING','Microsoft','Chrysler','Ofgas','British Gas']

# Dictionary to store all the context extracted in the form of key value pairs. The context for ING will be appended in the
# value list with key ING in the dictionary top5
top5={
    'ING':[],'Microsoft':[],'Chrysler':[],'Ofgas':[],'British Gas':[]}
print(companies)

# A loop which incrementally loops through each file path created by concatenating the homepath and filenames
for z in range(len(filelist)):
    mytext = open(mypath + filelist[z], "r") # This reads each file
    mytext = mytext.read()

    # POS tagging each file using the object NLP of spaCy
    docs=nlp(mytext)
    for x in docs.ents:
       #  Comparing the text of each article fetched with the list created of the top5 companies
       for i in range(5):
         if(x.text==companies[i]):
            for a in docs:
                # In each article, comparing each word and ensuring it is not a punctuation or a stop word
                if(a.is_stop != True and a.is_punct != True):

                    # To determine context, if company name is matched in the file, this code will search for tags to extract
                    # propernouns, common nouns, verbs, numbers or symbols which can help decipher the context
                    if( a.pos_ == 'PROPN' or a.pos_ == 'NOUN' or a.pos=='VERB'  or a.pos_ == 'NUM' or a.pos_ == 'SYM'):

                        #print(a, end=' ')

                        # Once context is extracted, it will again search the company name to append to the value space of
                        # the dictionary # which has the same key
                        if (x.text == companies[i]):
                            top5[companies[i]].append(a)
                            file=open('D:/Aditya/AUT/Text mining/Assignment 2 data/'+companies[i]+'.txt', "a+")
                            file.write(str(a)+' ')
                            file.close()

         #Breaking out of the loop once context extrated
         if (x.text == companies[i]):
            break

       if (x.text == companies[i]):
           break

# Appending the dictionary with the context
for j in range(5):
    print(companies[j],':',top5[companies[j]])
