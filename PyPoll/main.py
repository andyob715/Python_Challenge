# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

# Create some lists
Candidate = []
Candidate_Deets = []
#Reading using CSV module
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile)

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
#   print(f"CSV Header: {csv_header}")

#   Need to have a list of candidate values in a place where i can use it in my counter
    first_row = next(csvreader)
    
    for row in csvreader:
            Candidate.append(row[2])

#import the counter to find the count of indvidual values in the list
from collections import Counter
l = Candidate
mycount=Counter(l)

#Find the max index value of the candidates
MaxVoteCount = max(mycount, key=mycount.get)

#Find the Sum of all votes from the counter
s=sum(mycount.values())

#print the stuff to the terminal
topline=(f"Election Results\n"
f"---------------------\n"
f"Total Vote Count: {s}\n"
f"---------------------")
print(topline)
for k, v in mycount.items():
    pct = v * 100.0 / s
    counter_results = f"{k}: {pct}% ({v} votes)"
    print(counter_results)
bottomline=(f"---------------------\n"
f"Winner: {MaxVoteCount}\n")
print(bottomline)

# Specify the file to write to
output_path = os.path.join("Analysis", "pollresults.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtfile:
     txtfile.writelines(topline)
with open(output_path, 'a') as txtfile:
    for k, v in mycount.items():
        pct = v * 100.0 / s
        counter_results = f"{k}: {pct}% ({v} votes)"
    txtfile.writelines(counter_results)
with open(output_path, 'a') as txtfile:
    txtfile.writelines(bottomline)