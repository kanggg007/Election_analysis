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

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    header = next(file_reader)
    print(header)
