# The Data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of canadidates who recevied votes
# 3. The percentage of votes each canaidate won
# 4. The total number of votes each canaidate won
# 5. The winner of the election based on popluar vote

import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

total_votes = 0
Canadidate_option= []
candidate_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    header = next(file_reader)


    
    for row in file_reader:
        total_votes +=1 
        canadidates_name = row[2]

        if canadidates_name not in Canadidate_option:
            Canadidate_option.append(canadidates_name)
            candidate_votes[canadidates_name] = 0

        candidate_votes[canadidates_name] +=1    


    for canadidates_name in candidate_votes:
        votes = candidate_votes[canadidates_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        print(f"{canadidates_name}: {vote_percentage:.1f}% ({votes:,})\n")
             
        if votes >= winning_count and vote_percentage >= winning_percentage:
            winning_count = votes
            winning_percentage = vote_percentage

            winning_candidate = canadidates_name

winning_summary = (
    f"-------------------\n"
    f"winner is {winning_candidate}\n"
    f"winner vote percentage is {winning_percentage}%\n"
    f"winner vote is {winning_count}\n"
    f"-------------------------\n")
print(winning_summary)


