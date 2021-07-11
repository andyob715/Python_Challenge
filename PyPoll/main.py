# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

# Create some lists
Candidate = []
#Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile)

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
#   print(f"CSV Header: {csv_header}")
#   Need to have a list of candidate values
    first_row = next(csvreader)
    
    for row in csvreader:
            Candidate.append(row[2])

from collections import Counter
l = Candidate
mycount=Counter(l)

MaxVoteCount = max(mycount, key=mycount.get)
#print(MaxVoteCount)

s=sum(mycount.values())
for k, v in mycount.items():
    pct = v * 100.0 / s
    counter_results = f"{k}: {pct}% ({v} votes)"
    print(counter_results)


results = (f"Election Results\n"
f"---------------------\n"
f"Total Votes: {s} \n"
f"---------------------\n"
f"{counter_results}\n"
f"---------------------\n"
f"Winner: {MaxVoteCount}\n") 

print(results)
# print([counter_results for k,v in mycount.items()])

 # Specify the file to write to
#output_path = os.path.join("Resources", "pollresults.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
#with open(output_path, 'w') as txtfile:

 #   txtfile.write(results)      