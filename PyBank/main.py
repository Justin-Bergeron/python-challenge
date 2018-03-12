
# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
import numpy as np
#csvpath = os.path.join('PyBank', 'budget_data_1.csv')

date1 = []
revenue1 = []
date2 = []
revenue2 = []

# Method 2: Improved Reading using CSV module
import csv
with open('budget_data_1.csv', newline='') as csvfile1: #change to budge

    # CSV reader specifies delimiter and variable that holds contents
    csvreader1 = csv.reader(csvfile1, delimiter=',')
    next(csvreader1, None)

    for row in csvreader1:
        date1.append(row[0])
        revenue1.append(int(row[1]))
#date1 = [x[:-2]+'20'+x[-2:] for x in date1]


with open('budget_data_2.csv', newline='') as csvfile2:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader2 = csv.reader(csvfile2, delimiter=',')
    next(csvreader2, None)

    for row in csvreader2:
        date2.append(row[0])
        revenue2.append(row[1])

#The total number of months included in the dataset
total_months = len(date1)

#The total amount of revenue gained over the entire period
total_revenue = sum(revenue1)

#The average change in revenue between months over the entire period
rev = [0,]
for i in range(len(revenue1)):
    #deltarev.append(revenue1[i:i+2])
    rev.append(int(revenue1[i]))
res = [ y-x for x, y in zip(rev, rev[1:])] 

#greatest and lessest change
deltarev = sum(res)/len(res)
maxdelta = (max(res))
mindelta = (min(res))
dick = dict(zip(date1, res))


maxmax = []
minmin = []
for k,v in dick.items():
        if int(maxdelta) == v:
            maxmax.append(k)
            maxmax.append(v)
        if int(mindelta) == v:
            minmin.append(k)
            minmin.append(v)

combined1 = zip(date1, revenue1)
combined2 = zip(date2, revenue2)

print(' Financial Analysis\n - - - - - - - - - - - - - - - - \n Total Months: {0}\n Total Revenue: {1}\n Average Revenue Change: {2}\n Greatest Increase in Revenue: {3}\n Greatest Decrease in Revenue: {4}'.format(total_months, total_revenue, deltarev, maxmax, minmin))

f = open('Financial Analysis.txt','w')
f.write(' Financial Analysis\n - - - - - - - - - - - - - - - - \n Total Months: {0}\n Total Revenue: {1}\n Average Revenue Change: {2}\n Greatest Increase in Revenue: {3}\n Greatest Decrease in Revenue: {4}'.format(total_months, total_revenue, deltarev, maxmax, minmin))
f.close()

