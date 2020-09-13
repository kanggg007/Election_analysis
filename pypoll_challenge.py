import os 
import csv

file_to_read = os.path.join("Resources", "election_results.csv")

file_to_upload = os.path.join("analysis", "election_challenage_analysis.txt")

total_votes = 0

candidates_option = []

candidates_votes ={}

country_list = []

country_votes = {}

winning_country_count = 0

winning_country_precentage = 0
largest_count_country = ""

winning_candidate = ""
winning_count = 0
winning_percentage = 0




with open(file_to_read, 'r') as election_data:
    reader = csv.reader(election_data)
    header = next(reader)
    

    for row in reader:
        total_votes += 1
        candidates_name = row[2]
    # extract country from each row
        candidates_country= row[1]
    
        if candidates_name not in candidates_option:
            candidates_option.append(candidates_name)
            candidates_votes[candidates_name] = 0
    
        candidates_votes[candidates_name] += 1

    
    #4a  Write a  decision statement that checks that the
    # country does not match any existing country in the country list
        if candidates_country not in country_list:
            country_list.append(candidates_country)
            country_votes[candidates_country] = 0
        
        country_votes[candidates_country] += 1

        

with open(file_to_upload, "w") as txtfile:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"\nCountry Votes \n")
    print(election_results, end="")
    txtfile.write(election_results)

    for candidates_country in country_votes:
        countryVotes = country_votes[candidates_country]
        country_vote_percentage = float(countryVotes) / float(total_votes) * 100
        country_result = (f"{candidates_country}:{country_vote_percentage:.1f}%:{countryVotes:,} \n")
        print(country_result) 
        txtfile.write(country_result) 
        if countryVotes >= winning_country_count and country_vote_percentage >= winning_country_precentage:
            winning_country_count = countryVotes
            winning_country_precentage = country_vote_percentage
            largest_count_country = candidates_country
    winning_country_summary = (
        f"-----------------------------------\n"
        f"largest country turnout is {largest_count_country}\n"
        f"------------------------------\n")
    txtfile.write(winning_country_summary)
    print(winning_country_summary)
        
    for candidates_name in candidates_votes:
        votes = candidates_votes[candidates_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f"{candidates_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txtfile.write(candidate_results) 
        if votes >= winning_count and vote_percentage >= winning_percentage:
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidates_name

    winning_summary = (
        f"-------------------\n"
        f"winner is {winning_candidate}\n"
        f"winner vote is {winning_count}\n"
         f"winner vote percentage is {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_summary)
    txtfile.write(winning_summary) 


        