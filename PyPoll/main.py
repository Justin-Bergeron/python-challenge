# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
import numpy
from collections import Counter
import numpy as np

# csvpath = os.path.join('PyBank', 'budget_data_1.csv')

ID = []
county = []
candidate = []
rec_vote = []

# Method 2: Improved Reading using CSV module
import csv

with open('election_data_2.csv', newline='') as csvfile1:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader1 = csv.reader(csvfile1, delimiter=',')
    next(csvreader1, None)

    for row in csvreader1:
        ID.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

#The total number of Votes Cast
total_votes = len(ID)
#print(total_votes)
'''
# A complete list of candidates who received votes #Don't need this anymore
for x in candidate:
    if x not in rec_vote:
        rec_vote.append(x)
print(rec_vote) 
'''
#The percentage of votes each candidate won
c = Counter(candidate)
percent = [(i, c[i] / len(candidate) * 100.0) for i, count in c.most_common()]
percent = dict(percent)
#print(percent)  
        
#The total number of votes each candidate won
count = Counter()
for x in candidate:
    count[x] += 1
total = dict(count)
#print(total)
result = {}
for key in (percent.keys() | total.keys()):
    if key in percent: result.setdefault(key, []).append(percent[key])
    if key in total: result.setdefault(key, []).append(total[key])
#print(result)
# the winner        
winner = next(iter(percent))
#print(winner[0])

#unique_candidate = []
#for i in candidate:
#    if i not in unique_candidate:
#        unique_candidate.append(i)
#print(unique_candidate)        


#winner = list(percent.keys())[0]  

print(' Election Results\n - - - - - - - - - - - - - - - - \n Total Votes: {0}\n - - - - - - - - - - - - - - - -\n'.format(total_votes))
print("Name\tPercent\tVote Count")
for i in result:
    print("{}\t{}\t".format(i,result[i]))
print('- - - - - - - - - - - - - - - -\nWinner: {0}\n- - - - - - - - - - - - - - - -'.format(winner))    

f = open('Election Results.txt','w')
f.write(' Election Results\n - - - - - - - - - - - - - - - - \n Total Votes: {0}\n - - - - - - - - - - - - - - - -\n'.format(total_votes))
f.write("Name\tPercent\tVote Count")
for i in result:
    f.write("{}\t{}\t".format(i,result[i]))
f.write('- - - - - - - - - - - - - - - -\nWinner: {0}\n- - - - - - - - - - - - - - - -'.format(winner))    
f.close()