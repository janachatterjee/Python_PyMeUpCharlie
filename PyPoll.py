###PyPoll###
#-------------------------------------------------------------------------------------------------------#
#Dependencies - Import the os module so you can create file paths across operating systems/
############# - Import the csv module so the code can read the csv file
#-------------------------------------------------------------------------------------------------------#
import os
import csv

#Outline the path to the csv file you're going to use in the code
#-------------------------------------------------------------------------------------------------------#
csvpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'Resources', 'election_data.csv')

file_to_output = "analysis/election_analysis.txt"

#Make a Counter for the total number of votes cast
total_votes = 0

#Establish a complete list of candidates who received votes
candidate_options = []
candidate_votes = {}

#Make a Counter for Winning 
winning_candidate = ""
winning_count = 0

#Read the csv data into the dictionary and calculate
with open(file_to_load) as election_data:
    reader = csv.DictReader(election_data)

    for row in reader:

        #Run load results
        print(". ", end=""),

        #Add +1 to total vote count
        total_votes = total_votes + 1

        #Get the Candidate name from each row
        candidate_name = row["Candidate"]

        #If statement to 
        if candidate_name not in candidate_options:

            #Add to list of candidates 
            candidate_options.append(candidate_name)

            #Now, track the voter count
            candidate_votes[candidate_name] = 0

        #Now, add the votes to candidate's count
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

#Print Results & Export to text file
with open(file_to_output, "w") as txt_file:

    #Print final vote count
    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(election_results, end="")

    #Save final vote count to text file
    txt_file.write(election_results)

    #Calculate winner from counts
    for candidate in candidate_votes:

        #Calculate Vote Count/Percentage
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        #Get Winner and Vote Count
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        #Print vote count and % for all candidates
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")

        #Save all voter count/% to text file
        txt_file.write(voter_output)

    #Print Winner
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    #Save Winner to text file
    txt_file.write(winning_candidate_summary)