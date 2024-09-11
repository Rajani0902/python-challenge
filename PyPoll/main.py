import os
import csv

# Define the path to the CSV file
csvpath = os.path.join('..', 'Resources', 'election_data.csv')
# Initialize variables
total_votes = 0
votes_per_candidate = {}

# Open and read the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row
    csv_header = next(csvreader)
    
    # Process each row in the CSV file
    for row in csvreader:
        total_votes += 1
        candidate = row[2]
        if candidate not in votes_per_candidate:
            votes_per_candidate[candidate] = 1
        else:
            votes_per_candidate[candidate] += 1

# Print results to the console
print("Election Results")
print("---------------------------------------")
print(f"Total Votes: {total_votes}")
print("---------------------------------------")

for candidate, votes in votes_per_candidate.items():
    percentage = votes / total_votes
    print(f"{candidate}: {percentage:.3%} ({votes})")

print("-----------------------------------------")

# Determine and print the winner
winner = max(votes_per_candidate, key=votes_per_candidate.get)
print(f"Winner: {winner}")

# Define the output file path
output_file = 'Analysis_election_results.txt'

# Write results to the output file
with open(output_file, 'w') as f:
    f.write("Election Results\n")
    f. write("------------------------------------------\n")
    f.write(f"Total Votes: {total_votes}\n")
    f.write("--------------------------------------------\n")
    
    for candidate, votes in votes_per_candidate.items():
        percentage = votes / total_votes
        f.write(f"{candidate}: {percentage:.3%} ({votes})\n")
    
    f.write("----------------------------------\n")
    f.write(f"Winner: {winner}\n")