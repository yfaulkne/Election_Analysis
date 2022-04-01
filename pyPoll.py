# The data we need to retrieve
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on the popular vote

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize the total vote counter before opeining the file because everytime we run the file, the total_votes variable must be set equal to zero
total_votes = 0

#Declare a new list of candidate options
candidate_options = []

#Declare an empty dictionary
candidate_votes = {}

#Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0 
winning_percentage = 0 

# Open the election results and read the file.
election_data = open(file_to_load, 'r')
read_file = csv.reader(election_data)

# Read the header row.
headers = next(read_file)

#Print each row in the CSV file
for row in read_file:
    #Add to the total vote count
    total_votes += 1

    #Print the candidate name from each row. index 2 is fro the 2nd column in the file. We are looking at each row in column 2
    candidate_name = row[2]

    #If the candidate does not match any existing candidate...
    if candidate_name not in candidate_options:
        
        #Add it to the list of candidates
        candidate_options.append(candidate_name)

        #Begin tracking that candidate's vote count
        candidate_votes[candidate_name] = 0

    #Add a vote to that candidate's count
    candidate_votes[candidate_name] += 1 

#Determine the percentage of votes for each candidate by looping through the counts
#1. Iterate through the candidate votes
for candidate_name in candidate_votes:
    #2. Retrieve the vote count of a candidate
    votes = candidate_votes[candidate_name]
    #3. Calculate the percentage of votes
    vote_percentage = float(votes) / float(total_votes) * 100

    #To do: print out each candidate's name, vote count, and percentage of votes to the terminal
    print(f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n')


    #Determine winning vote count and candidate
    #Deteremine if the votes is greater than the winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        #If true then set winning_count = votes and winning_percent = vote percentage
        winning_count = votes
        winning_percentage = vote_percentage
        #And set the winning_candidate equal to the candidate's name
        winning_candidate = candidate_name

#To do: print out the winning candidate, vote count and percentage to terminal
winning_candidate_summary = (
     f'-------------------------\n'
     f'Winner: {winning_candidate}\n'
     f'Winning Vote Count : {winning_count:,}\n'
     f'Winning Percentage: {winning_percentage:.1f}%\n'
     f'-------------------------\n')
#4. Print the candidate name and percentage of votes
print(winning_candidate_summary)  






