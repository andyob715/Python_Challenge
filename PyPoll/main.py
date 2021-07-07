import os
import csv

file_to_load = os.path.join("Resources", "election_data.csv")

# # new lists

# voter_id = []
# voter_county = []
# voter_candidate = []


# Open and read csv
with open(file_to_load) as poll_data:
    csv_reader = csv.reader(poll_data, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_reader)
    print(f"Header: {csv_header}")

#   * A complete list of candidates who received votes
#   Need to have a list of candidate values

    candidate = []
    for row in csv_reader:
        candidate.append(csv_reader[2])

    print(candidate)

#   * The percentage of votes each candidate won

#   * The total number of votes each candidate won

#   * The winner of the election based on popular vote.

# * As an example, your analysis should look similar to the one below:

#   ```text
#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------
#   ```