# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

# Create some lists
voterid = []
County = []
Candidate = []
#Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile)

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
#   Need to have a list of candidate values
    first_row = next(csvreader)
    
    for row in csvreader:
            Candidate.append(row[2])
    
    Total_Votes=len(Candidate)
    
    print(Total_Votes)

#   * The percentage of votes each candidate won
# I need to find a way to take each individual candidate and count up how many times their name appears on the list and divide that by Total_VOtes
# How do I do this for each candidate, list comprehension? sum if? how do i cycle through each individual candidate??

#   * The total number of votes each candidate won


# results = (f"Election Results\n"
#     f"---------------------\n"
#     f"Total Votes: {Total_Votes} \n"
#     f"---------------------\n"
#     f"Print each person that got vote sin a list with percentage and total number\n"
#     f"---------------------\n"
#     f"Total Votes: \n")
   
# print(results)

 # Specify the file to write to
#output_path = os.path.join("Resources", "pollresults.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
#with open(output_path, 'w') as txtfile:

 #   txtfile.write(results)      