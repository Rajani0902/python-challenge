import os
# Module for reading CSV files
import csv
csv = os.path.join('..', 'Resources', 'budget_data.csv')

count = 0

with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
     # Read each row of data after the header
    for row in csvreader:
        count +=1
        print(row)

