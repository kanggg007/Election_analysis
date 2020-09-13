# Election_analysis
According to the data from Election_Challenage_analysis.txt that retrieved by applying python to analyzed election csv data frame, we easily concluded that the outcome of election 

 Election outcome:

•	How many votes were cast in this congressional election? 
We looped through the election csv file without heading and incremented votes it shows Total votes from this election is 369,711. 

•	Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct. Which county had the largest number of votes? 
By creating a dictionary to contain votes for each country under condition statement, we iterated data frame and figured out the number of votes for each country. The largest votes came from Denver which weighted more than 80 percent

•	Provide a breakdown of the number of votes and the percentage of the total votes each candidate received. 
There are only three candidates in this election, Charles Casper Stockham, Diana DeGette, and Raymon Anthony. Charles got 85,231 votes out of 369,711, which is 23 percent of total votes. Diana DeGette got 272,892 votes out of 369,711, which is 73.8 percent of total votes. Raymon Anthony got 11,606 votes out of 369,711, which is 3,1 percent of total votes.

•	Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
Same as worked out the largest country, we just modified the script a little bit to figure out the winner candidate. Diana DeGette won the election and she got more than 70 percent votes. 


Summary:

This script is working for this specific problem but is not efficient to work out other more complicated election. 
•	Instead of using loop through a couple of times, priority queue could be applied without taking longer time and space.
•	The script did not illustrate that how many votes each candidate get from each different country. We should modify to add a couple of lines to show it.

