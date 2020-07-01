import os
import csv

pypoll_csv = os.path.join('.', 'PyPoll', 'Resources', 'election_data.csv')

#set veriables, create lists and dictionaries
total_votes = 0
highest_votes = 0
candidates = [] #stores list of candidate names
ballot = {} #stores vote count per candidate
vote_percentage = [] #stores the votes per candidate/total votes
candidate_data = [] #stores candidate name, vote % and votes per candidate


with open(pypoll_csv) as pypoll:
    csvreader = csv.reader(pypoll, delimiter=',')
    next(pypoll)

    for row in csvreader:
        #count total votes
        total_votes += 1
        #find which candidate that voter chose
        candidate = row[2]
        #if candidate exists in directory, add 1 vote to their tally
        if candidate in ballot:
            ballot[candidate] += 1  
        #if candidate does npt exist in directory, set vote count = 1
        else:
            ballot[candidate] = 1
        #if candidate is not in candidates list, add them
        if not candidate in candidates:
            candidates.append(candidate) 
        
    #need to create loop that goes through candidate list and adds vote % and votes per candidate
    #need to convert candidates list into integers
    for candidate in range(len(candidates)):
        #calculate % by taking the # of votes for each candidate in ballot list / total
        vote_percentage.append(ballot[candidates[candidate]] / total_votes)
        #formatting
        vote_percentage[candidate] = format(vote_percentage[candidate], ".3%")
        #append candidate name, vote % and total votes to data list
        candidate_data.append(f"{candidates[candidate]}: {vote_percentage[candidate]} ({ballot[candidates[candidate]]})")

    #determine winner by looping through ballot to see which candidate has the highest votes, starting at 0
    for candidate in candidates:
        if ballot[candidate] > highest_votes:
            highest_votes = ballot[candidate]
            winner_name = candidate

#print in terminal
print(f"Election Results")
print(f"---------------------------")
print(f"Total Votes: {total_votes}")
print(f"---------------------------")
for candidate in range(len(candidates)):
    print(f"{candidate_data[candidate]}")
print(f"---------------------------")
print(f"Winner: {winner_name}")
print(f"---------------------------")

#set ouput path
output_file = os.path.join('.', 'PyPoll', 'Analysis', 'election_data_analysis.txt')

#print .txt
with open(output_file, 'w',) as txtfile:
    txtfile.write(f"Election Results\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write(f"---------------------------\n")
    for candidate in range(len(candidates)):
        txtfile.write(f"{candidate_data[candidate]}\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Winner: {winner_name}\n")
    txtfile.write(f"---------------------------\n")