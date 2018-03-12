import os
import numpy as np
import re

'''  if you want a csv file
# Import a text file filled with a paragraph of your choosing. 
import csv

results = []
with open('words.txt', newline='') as inputfile:
    for row in csv.reader(inputfile):
        results.append(row)

print(results)        

output_file = os.path.join('words.csv')
with open(output_file, "w", newline="", encoding="utf-8") as results:
    writer = csv.writer(results)
    writer
'''

#strip().split(',') methods for line if you need them
words = []
with open('paragraph_2.txt') as inputfile:
    for i in inputfile:
        words.append(i)
#print(words)        


# Approximate word count 
for i in words:
    chopchop = str(words).split()
wc = len(chopchop)  #add 1 for the last word that doesn't have space after it
#print(wc)

# Approximate sentence count 
s = re.findall('[.?!]', str(words))   # i was tired of trying to do this in one line
#s1 = re.findall(r'\!', str(words))
#s2 = re.findall(r'\?', str(words))
sc =len(s)
#print(sc)


# Approximate letter count (per word) 
lc = []
#print(chopchop)
for i in chopchop:
    #re.match('[A-Za-z] + [^]', str(i))   #just count the regular expression match
   # if re.match("[.!?]", str(i):    
   lc = len(re.findall('[A-Za-z]', str(i)))
lecoword = np.mean(lc)
#print(lecoword)


# Average sentence length (in words)
pow = []
sentence = re.split("(?<=[.!?]) +", str(words))
for i in sentence:
    cutcut = str(i).split()
    senlen = len(cutcut) 
     #add 1 for the last word that doesn't have space after it
    pow.append(senlen)
avgsenlen = np.mean(pow)
#print(avgsenlen)

print('Approximate Word Count: {0}\nApproximate Sentence Count: {1}\nAverage Letter Count: {2}\nAverage Sentence Length: {3}\n'.format(wc, sc, lecoword, avgsenlen))